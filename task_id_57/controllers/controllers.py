# -*- coding: utf-8 -*-
# from odoo import http


# class TaskId57(http.Controller):
#     @http.route('/task_id_57/task_id_57', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/task_id_57/task_id_57/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('task_id_57.listing', {
#             'root': '/task_id_57/task_id_57',
#             'objects': http.request.env['task_id_57.task_id_57'].search([]),
#         })

#     @http.route('/task_id_57/task_id_57/objects/<model("task_id_57.task_id_57"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('task_id_57.object', {
#             'object': obj
#         })
