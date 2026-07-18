from odoo import models, fields


class GarageServiceType(models.Model):
    _name = "garage.service.type"
    _description = "Garage Service Type"
    _order = "name"

    name = fields.Char(required=True)
    code = fields.Char(required=True)
    price = fields.Monetary(required=True)
    currency_id = fields.Many2one("res.currency", string="Currency", required=True)
    duration = fields.Float(required=True)
    active = fields.Boolean(default=True)
