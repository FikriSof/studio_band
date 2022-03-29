# -*- coding: utf-8 -*-
# from odoo import http


# class StudioBand(http.Controller):
#     @http.route('/studio_band/studio_band/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/studio_band/studio_band/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('studio_band.listing', {
#             'root': '/studio_band/studio_band',
#             'objects': http.request.env['studio_band.studio_band'].search([]),
#         })

#     @http.route('/studio_band/studio_band/objects/<model("studio_band.studio_band"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('studio_band.object', {
#             'object': obj
#         })
