from odoo import api, fields, models
from odoo.exceptions import ValidationError

class Order(models.Model):
    _name = 'studioband.order'
    _description = 'New Description'

    orderstudiodetail_ids = fields.One2many(
        comodel_name='studioband.orderstudiodetail', 
        inverse_name='orders_id', 
        string='Sewa Studio Musik')
    
    orderalatdetail_ids = fields.One2many(
        comodel_name='studioband.orderalatdetail', 
        inverse_name='ordera_id', 
        string='Sewa Alat Musik')
    
    name = fields.Char(string='Kode Order', required=True)
    tanggal_book = fields.Datetime('Tanggal Booking',default=fields.Datetime.now())
    tanggal_main = fields.Date(string='Tanggal Main', default=fields.Date.today())
    
    pemesan = fields.Many2one(comodel_name='res.partner', string='Nama Pemesan', domain=[('is_customer','=', True)],store=True)
    

    total = fields.Integer(compute='_compute_total', string='Total', store=True)
    
    @api.depends('orderstudiodetail_ids')
    def _compute_total(self):
        for record in self:
            a = sum(self.env['studioband.orderstudiodetail'].search([('orders_id', '=', record.id)]).mapped('harga'))
            b = sum(self.env['studioband.orderalatdetail'].search([('ordera_id', '=', record.id)]).mapped('harga'))
            record.total = a + b

    sudah_selesai = fields.Boolean(string='Orderan Telah Selesai', default=False)
    

class OrderStudioDetail(models.Model):
    _name = 'studioband.orderstudiodetail'
    _description = 'New Description'

    orders_id = fields.Many2one(comodel_name='studioband.order', string='Order')
    studio_id = fields.Many2one(comodel_name='studioband.studiomusik', string='Studio Musik')

    name = fields.Char(string='Name')
    harga = fields.Integer(compute='_compute_harga', string='Total')
    qty = fields.Integer(string='Room')
    waktu_sewa = fields.Integer(string='Jam')
    
    harga_satuan = fields.Integer(compute='_compute_harga_satuan', string='Harga')

    @api.depends('studio_id')
    def _compute_harga_satuan(self):
        for record in self:
            record.harga_satuan = record.studio_id.harga
    
    @api.depends('qty','harga_satuan','waktu_sewa')
    def _compute_harga(self):
        for record in self:
           record.harga = record.harga_satuan * record.qty * record.waktu_sewa
    
    @api.model
    def create(self,vals):
        record = super(OrderStudioDetail, self).create(vals) 
        if record.qty:
            self.env['studioband.studiomusik'].search([('id','=',record.studio_id.id)]).write({'stok':record.studio_id.stok-record.qty})
            return record
    
class OrderAlatDetail(models.Model):
    _name = 'studioband.orderalatdetail'
    _description = 'New Description'

    ordera_id = fields.Many2one(comodel_name='studioband.order', string='Order Alat Musik')
    alatmusik_id = fields.Many2one(comodel_name='studioband.alatmusik', string='Alat Musik')

    name = fields.Char(string='Name')
    waktu_sewa = fields.Integer(string='Jam')
    harga_satuan = fields.Integer(compute='_compute_harga_satuan', string='Harga')
    
    @api.depends('alatmusik_id')
    def _compute_harga_satuan(self):
        for record in self:
            record.harga_satuan = record.alatmusik_id.harga
    
    qty = fields.Integer(string='Banyak')

    @api.constrains('qty')
    def _check_stok(self):
        for record in self:
            bahan = self.env['studioband.alatmusik'].search([('stok', '<',record.qty),('id', '=',record.id)])
            if bahan:
                raise ValidationError("Stok Alat Musik Yang Dipilih Kosong")
    
    harga = fields.Integer(compute='_compute_harga', string='Total')

    @api.depends('harga_satuan','qty','waktu_sewa')
    def _compute_harga(self):
        for record in self:
               record.harga = record.harga_satuan * record.qty * record.waktu_sewa
    
    @api.model
    def create(self,vals):
        record = super(OrderAlatDetail, self).create(vals) 
        if record.qty:
            self.env['studioband.alatmusik'].search([('id','=',record.alatmusik_id.id)]).write({'stok':record.alatmusik_id.stok-record.qty})
            return record