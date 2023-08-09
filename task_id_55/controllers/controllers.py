# -*- coding: utf-8 -*-
# from odoo import http


# class TaskId55(http.Controller):
#     @http.route('/task_id_55/task_id_55', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/task_id_55/task_id_55/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('task_id_55.listing', {
#             'root': '/task_id_55/task_id_55',
#             'objects': http.request.env['task_id_55.task_id_55'].search([]),
#         })

#     @http.route('/task_id_55/task_id_55/objects/<model("task_id_55.task_id_55"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('task_id_55.object', {
#             'object': obj
#         })
