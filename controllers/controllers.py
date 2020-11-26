# -*- coding: utf-8 -*-
from odoo import http

# class FleetManagementCu(http.Controller):
#     @http.route('/fleet_management_cu/fleet_management_cu/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fleet_management_cu/fleet_management_cu/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fleet_management_cu.listing', {
#             'root': '/fleet_management_cu/fleet_management_cu',
#             'objects': http.request.env['fleet_management_cu.fleet_management_cu'].search([]),
#         })

#     @http.route('/fleet_management_cu/fleet_management_cu/objects/<model("fleet_management_cu.fleet_management_cu"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fleet_management_cu.object', {
#             'object': obj
#         })