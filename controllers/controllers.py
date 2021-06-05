# -*- coding: utf-8 -*-
# from odoo import http


# class Get-weather(http.Controller):
#     @http.route('/get-weather/get-weather/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/get-weather/get-weather/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('get-weather.listing', {
#             'root': '/get-weather/get-weather',
#             'objects': http.request.env['get-weather.get-weather'].search([]),
#         })

#     @http.route('/get-weather/get-weather/objects/<model("get-weather.get-weather"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('get-weather.object', {
#             'object': obj
#         })
