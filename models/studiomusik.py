from odoo import api, fields, models


class StudioMusik(models.Model):
    _name = 'studioband.studiomusik'
    _description = 'New Description'

    name = fields.Char(string='Name', required=True)
    paketband_id = fields.Many2one(comodel_name='studioband.paketband', string='Paket Band', required=True)
    deskripsi = fields.Char(string='Deskripsi')
    stok = fields.Integer(string='Ketersediaan Room')
    harga = fields.Char(compute='_compute_harga', string='Harga')
    
    @api.depends('paketband_id')
    def _compute_harga(self):
        for record in self:
            record.harga = record.paketband_id.harga + 30000
    
    des_paketband = fields.Char(compute='_compute_des_paketband', string='Deskripsi Paket Band')
    
    @api.depends('paketband_id')
    def _compute_des_paketband(self):
        for record in self:
            record.des_paketband = record.paketband_id.deskripsi