# -*- coding: utf-8 -*-
# from odoo import http


# class IdsInheritInventory(http.Controller):
#     @http.route('/ids_inherit_inventory/ids_inherit_inventory', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ids_inherit_inventory/ids_inherit_inventory/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ids_inherit_inventory.listing', {
#             'root': '/ids_inherit_inventory/ids_inherit_inventory',
#             'objects': http.request.env['ids_inherit_inventory.ids_inherit_inventory'].search([]),
#         })

#     @http.route('/ids_inherit_inventory/ids_inherit_inventory/objects/<model("ids_inherit_inventory.ids_inherit_inventory"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ids_inherit_inventory.object', {
#             'object': obj
#         })
