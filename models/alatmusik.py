from odoo import api, fields, models


class AlatMusik(models.Model):
    _name = 'studioband.alatmusik'
    _description = 'New Description'

    name = fields.Char(string='Name', required=True)
    harga = fields.Integer(string='Harga Sewa/Jam')
    stok = fields.Integer(string='Stok Barang')
    