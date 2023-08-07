from odoo import models, fields, api

class Users(models.Model):
    _inherit = 'res.users'

    # new fields
    warehouse_ids = fields.Many2many('stock.warehouse', string='Default-Warehouses')

    @property
    def location_ids(self):
        if self.warehouse_ids:
            return self.env['stock.location'].search([]).filtered(lambda x:x.warehouse_id in self.warehouse_ids)
        else:
            return self.env['stock.location'].search([])

    @api.onchange('warehouse_ids')
    def _clear_rule_cache(self):
        self.env['ir.rule'].clear_cache()