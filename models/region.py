from odoo import models, fields

class ResRegion(models.Model):
    _name = 'res.region'
    _description = 'Region'

    name = fields.Char(string='Region Name', required=True)
    code = fields.Char(string='Region Code', required=True)

    _sql_constraints = [
        ('code_uniq', 'unique (code)', 'Region code must be unique.')
    ]