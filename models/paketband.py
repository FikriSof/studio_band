from odoo import api, fields, models


class PaketBand(models.Model):
    _name = 'studioband.paketband'
    _description = 'New Description'

    name = fields.Char(string='Name', required=True)
    paket = fields.Selection(string='Paket Alat Band', selection=[('low', 'Kelengkapan Seadanya'), ('medium', 'Kelengkapan Standar'), ('high', 'Kelengkapan Lengkap'), ('custom', 'Kelengkapan Custom')])
    deskripsi = fields.Char(string='Deskripsi')
    harga = fields.Integer(string='Harga Sewa/Jam')
    stok = fields.Integer(string='Stok')
