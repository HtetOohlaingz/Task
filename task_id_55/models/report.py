from odoo import models, fields

class PurchaseReportInherit(models.Model):
    _inherit = 'purchase.report'

    price_unit = fields.Float(string='Unit Price')

    def _select(self):
        return super(PurchaseReportInherit, self)._select() + ", l.price_unit as price_unit"

    def _group_by(self):
        return super(PurchaseReportInherit, self)._group_by() + ", l.price_unit"

