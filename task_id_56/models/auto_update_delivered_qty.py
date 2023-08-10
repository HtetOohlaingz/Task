from odoo import models, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.onchange('order_line')
    def _onchange_order_line(self):
        for line in self.order_line:
            if line.product_id.type == 'product':
                service_line = self.order_line.filtered(lambda l: l.product_id.type == 'service')
                if service_line:
                    if line.product_uom_qty <= 30:
                        service_line.price_unit = 120000.0
                    else:
                        pass
                    
