from odoo import api, fields, models

class ResCusPartner(models.Model):
    _inherit = 'res.partner'

    commission = fields.Boolean('Commission')
