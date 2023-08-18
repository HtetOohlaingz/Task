from odoo import models, fields, api

class CustomSaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    line_number = fields.Integer(string='Line Number', compute='_compute_line_number')

    @api.depends('order_id.order_line')
    def _compute_line_number(self):
        for i, line in enumerate(self.order_id.order_line, start=1):
            line.line_number = i
