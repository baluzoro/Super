# -*- coding: utf-8 -*-
from odoo import http

# class StateValidate(http.Controller):
#     @http.route('/state_validate/state_validate/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/state_validate/state_validate/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('state_validate.listing', {
#             'root': '/state_validate/state_validate',
#             'objects': http.request.env['state_validate.state_validate'].search([]),
#         })

#     @http.route('/state_validate/state_validate/objects/<model("state_validate.state_validate"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('state_validate.object', {
#             'object': obj
#         })