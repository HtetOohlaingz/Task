# -*- coding: utf-8 -*-
# from odoo import http


# class TaskId53(http.Controller):
#     @http.route('/task_id_53/task_id_53', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/task_id_53/task_id_53/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('task_id_53.listing', {
#             'root': '/task_id_53/task_id_53',
#             'objects': http.request.env['task_id_53.task_id_53'].search([]),
#         })

#     @http.route('/task_id_53/task_id_53/objects/<model("task_id_53.task_id_53"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('task_id_53.object', {
#             'object': obj
#         })
