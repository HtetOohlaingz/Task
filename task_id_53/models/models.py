# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class task_id_53(models.Model):
#     _name = 'task_id_53.task_id_53'
#     _description = 'task_id_53.task_id_53'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
