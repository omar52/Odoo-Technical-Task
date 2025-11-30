from odoo import models, fields

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    enable_credit_limit = fields.Boolean(
        string='Enable Credit Limit on Customers',
        config_parameter='sales.enable_credit_limit'
    )