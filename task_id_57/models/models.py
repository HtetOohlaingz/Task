# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class task_id_57(models.Model):
#     _name = 'task_id_57.task_id_57'
#     _description = 'task_id_57.task_id_57'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
