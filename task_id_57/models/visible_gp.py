from odoo import models, fields, api

class VisibleGroup(models.Model):
    _name = 'visible.group'

    visible_field = fields.Char(string="Visible Field")

    user_can_see_field = fields.Boolean(
        string="User Can See Field",
        compute='_compute_user_can_see_field',
        store=False
    )

    # @api.depends('user_can_see_field')
    # def _compute_user_can_see_field(self):
    #     for record in self:
    #         record.user_can_see_field = self.env.user.has_group("account_group_manager")