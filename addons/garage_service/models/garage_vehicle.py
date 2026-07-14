from odoo import models, fields

class GarageVehicle(models.Model):
    _name = "garage.vehicle"
    _description = "Garage Vehicle"

    name = fields.Char(string="Name")
    brand = fields.Char(string="Brand", required=True)
    model = fields.Char(string="Model", required=True)
    plate = fields.Char(string="Plate", required=True)

