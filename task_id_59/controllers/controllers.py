# -*- coding: utf-8 -*-
# from odoo import http


# class TaskId59(http.Controller):
#     @http.route('/task_id_59/task_id_59', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/task_id_59/task_id_59/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('task_id_59.listing', {
#             'root': '/task_id_59/task_id_59',
#             'objects': http.request.env['task_id_59.task_id_59'].search([]),
#         })

#     @http.route('/task_id_59/task_id_59/objects/<model("task_id_59.task_id_59"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('task_id_59.object', {
#             'object': obj
#         })
