from odoo import models, fields


class GarageMechanic(models.Model):
    _name = 'garage.mechanic'
    _description = 'Garage Mechanic'
    _order = "name"

    name = fields.Char(required=True, string="Mechanic")
    phone = fields.Char(required=True)
    email = fields.Char()
    hire_date = fields.Date()
    photo = fields.Binary(attachment=True)
    specialization_ids = fields.Many2many("garage.service.type")
    active = fields.Boolean(default=True)
