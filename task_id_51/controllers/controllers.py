# -*- coding: utf-8 -*-
# from odoo import http


# class TaskId51(http.Controller):
#     @http.route('/task_id_51/task_id_51', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/task_id_51/task_id_51/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('task_id_51.listing', {
#             'root': '/task_id_51/task_id_51',
#             'objects': http.request.env['task_id_51.task_id_51'].search([]),
#         })

#     @http.route('/task_id_51/task_id_51/objects/<model("task_id_51.task_id_51"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('task_id_51.object', {
#             'object': obj
#         })
