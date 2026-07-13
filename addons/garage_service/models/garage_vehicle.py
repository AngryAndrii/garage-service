from odoo import models, fields

class GarageVehicle(models.Model):
    _name = "garage.vehicle"
    _description = "Garage Vehicle"

    name = fields.Char(string="Name")
