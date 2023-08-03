# -*- coding: utf-8 -*-
# from odoo import http


# class TaskId52(http.Controller):
#     @http.route('/task_id_52/task_id_52', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/task_id_52/task_id_52/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('task_id_52.listing', {
#             'root': '/task_id_52/task_id_52',
#             'objects': http.request.env['task_id_52.task_id_52'].search([]),
#         })

#     @http.route('/task_id_52/task_id_52/objects/<model("task_id_52.task_id_52"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('task_id_52.object', {
#             'object': obj
#         })
