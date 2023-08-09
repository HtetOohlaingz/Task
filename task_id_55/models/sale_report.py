from odoo import models, fields

class SaleReportInherit(models.Model):
    _inherit = 'sale.report'

    price_unit = fields.Float(string='Unit Price')

    def _select_additional_fields(self):
        res = super()._select_additional_fields()
        
        res['price_unit'] = "l.price_unit"
        return res

    def _group_by_sale(self):
        res = super()._group_by_sale()
        res += """,
            l.price_unit """
        return res


