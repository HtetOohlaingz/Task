from odoo import api, fields, models, SUPERUSER_ID

class ResUsers(models.Model):
    _inherit = 'res.users'

    default_warehouse_id = fields.Many2one('stock.warehouse', string='Default Warehouse')
    operation_type = fields.Selection([
        ('receipt', 'Receipt'),
        ('delivery', 'Delivery'),
        ('internal_transfer', 'Internal Transfer')],
        string='Operation Type')

    @api.onchange('default_warehouse_id')
    def _onchange_default_warehouse_id(self):
        # Automatically set the operation type based on the warehouse type
        if self.default_warehouse_id:
            if self.default_warehouse_id.reception_steps == 'one_step':
                self.operation_type = 'receipt'
            elif self.default_warehouse_id.delivery_steps == 'ship_only':
                self.operation_type = 'delivery'
            else:
                self.operation_type = 'internal_transfer'

    def set_default_warehouse_and_operation_type(self, default_warehouse_id, operation_type):
        # Update the user's default warehouse and operation type
        self.write({'default_warehouse_id': default_warehouse_id, 'operation_type': operation_type})

# Usage example
# To set default warehouse and operation type for a user with ID 1
user_id = 6
default_warehouse_id = 3  # Replace with the actual ID of the desired warehouse
operation_type = 'receipt'  # Choose from 'receipt', 'delivery', or 'internal_transfer'

env = api.Environment(models.registry('Task'), SUPERUSER_ID, {})

# Get the user object
user = env['res.users'].browse(user_id)

# Call the method to set default warehouse and operation type
user.set_default_warehouse_and_operation_type(default_warehouse_id, operation_type)
