# -*- coding: utf-8 -*-
# from odoo import http


# class TaskId56(http.Controller):
#     @http.route('/task_id_56/task_id_56', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/task_id_56/task_id_56/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('task_id_56.listing', {
#             'root': '/task_id_56/task_id_56',
#             'objects': http.request.env['task_id_56.task_id_56'].search([]),
#         })

#     @http.route('/task_id_56/task_id_56/objects/<model("task_id_56.task_id_56"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('task_id_56.object', {
#             'object': obj
#         })
