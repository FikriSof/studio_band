from odoo import api, fields, models


class OrderSelesai(models.Model):
    _name = 'studioband.orderselesai'
    _description = 'Orderan Selesai'

    name = fields.Char(compute='_compute_nama_penyewa', string='Nama Penyewa')
    order_id = fields.Many2one(comodel_name='studioband.order', string='No. Order')
    
    @api.depends('order_id')
    def _compute_nama_penyewa(self):
        for record in self:
            record.name = self.env['studioband.order'].search([('id', '=', record.order_id.id)]).mapped('pemesan').name
    
    tgl_selesai = fields.Date(string='', default=fields.Date.today())

    tagihan = fields.Integer(compute='_compute_tagihan', string='Tagihan')
    
    @api.depends('order_id')
    def _compute_tagihan(self):
        for record in self:
            record.tagihan = record.order_id.total

    @api.model
    def create(self,vals):
        record = super(OrderSelesai, self).create(vals) 
        if record.tgl_selesai:
            self.env['studioband.order'].search([('id','=',record.order_id.id)]).write({'sudah_selesai':True})          
            return record

    def unlink(self):
        for i in self:
            self.env['studioband.order'].search([('id','=',i.order_id.id)]).write({'sudah_selesai':False})
        record = super(OrderSelesai, self).unlink()
