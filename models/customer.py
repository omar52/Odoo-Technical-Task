from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    credit_limit = fields.Float(string='Credit Limit', groups="odoo_technical_task.group_edit_credit_limit")
    region_id = fields.Many2one('res.region', string='Region')