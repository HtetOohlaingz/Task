# -*- coding: utf-8 -*-
# from odoo import http


# class TaskId60(http.Controller):
#     @http.route('/task_id_60/task_id_60', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/task_id_60/task_id_60/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('task_id_60.listing', {
#             'root': '/task_id_60/task_id_60',
#             'objects': http.request.env['task_id_60.task_id_60'].search([]),
#         })

#     @http.route('/task_id_60/task_id_60/objects/<model("task_id_60.task_id_60"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('task_id_60.object', {
#             'object': obj
#         })
