from odoo import api, fields, models


class AccountCommission(models.Model):
    _inherit = 'account.move'

    cus_ref = fields.Many2one('res.partner', string='Customer Reference')

    def generate_vendor_bill(self, partner_id):
        vendor_bill_vals = {
            'partner_id': partner_id,
            'move_type': 'in_invoice',  # Adjust with the correct field
            # Add other necessary fields
        }
        vendor_bill = self.env['account.move'].create(vendor_bill_vals)
        return vendor_bill

    def action_post(self):
        res = super(AccountCommission, self).action_post()

        vendor_bill = False
        for acc in self.filtered(lambda x: x.cus_ref.id and x.cus_ref.commission):
            customer_invoices = self.env['account.move'].search([
                ('partner_id', '=', acc.partner_id.id),
                ('state', '=', 'posted'),
                ('move_type', '=', 'out_invoice')
            ])
            if customer_invoices:
                vendor_bill = self.generate_vendor_bill(acc.partner_id.id)

        return res, vendor_bill