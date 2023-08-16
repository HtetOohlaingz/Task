# -*- coding: utf-8 -*-
# from odoo import http


# class TaskId58(http.Controller):
#     @http.route('/task_id_58/task_id_58', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/task_id_58/task_id_58/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('task_id_58.listing', {
#             'root': '/task_id_58/task_id_58',
#             'objects': http.request.env['task_id_58.task_id_58'].search([]),
#         })

#     @http.route('/task_id_58/task_id_58/objects/<model("task_id_58.task_id_58"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('task_id_58.object', {
#             'object': obj
#         })
