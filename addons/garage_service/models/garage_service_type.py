from odoo import models, fields


class GarageServiceType(models.Model):
    _name = "garage.service.type"
    _description = "Garage Service Type"

    name = fields.Char(required=True)
    code = fields.Char(required=True)
    price = fields.Float(required=True)
    monetary = fields.Float(required=True)
    duration = fields.Float(required=True)
    active = fields.Boolean(default=True)
