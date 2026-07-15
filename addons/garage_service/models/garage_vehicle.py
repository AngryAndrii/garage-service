from odoo import models, fields


class GarageVehicle(models.Model):
    _name = "garage.vehicle"
    _description = "Garage Vehicle"

    name = fields.Char(string="Name")
    brand = fields.Char(string="Brand", required=True)
    model = fields.Char(string="Model", required=True)
    plate = fields.Char(string="Plate", required=True)
    year = fields.Integer(string="Year", required=True)
    fuel_type = fields.Selection([
        ("gasoline", "Gasoline"),
        ("diesel", "Diesel"),
        ("electric", "Electric"),
        ("hybrid", "Hybrid"),
    ])
    mileage = fields.Integer(string="Mileage", required=True)
    owner_id = fields.Many2one("res.partner", required=True, ondelete="restrict")
    owner_phone = fields.Char(related="owner_id.phone", string="Phone")
    # repair_order_ids = fields.One2many("garage.repair.order", inverse="garage.vehicle_id")
    repair_count = fields.Integer(compute="_compute_repair_count")

    def _compute_repair_count(self):
        for vehicle in self:
            vehicle.repair_count = 0