# -*- coding: utf-8 -*-
# from odoo import http


# class TaskId54(http.Controller):
#     @http.route('/task_id_54/task_id_54', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/task_id_54/task_id_54/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('task_id_54.listing', {
#             'root': '/task_id_54/task_id_54',
#             'objects': http.request.env['task_id_54.task_id_54'].search([]),
#         })

#     @http.route('/task_id_54/task_id_54/objects/<model("task_id_54.task_id_54"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('task_id_54.object', {
#             'object': obj
#         })
