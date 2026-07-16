from odoo import models, fields, api


class GarageVehicle(models.Model):
    _name = "garage.vehicle"
    _description = "Garage Vehicle"

    name = fields.Char(string="Name", compute="_compute_name")
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
    repair_order_ids = fields.One2many("garage.repair.order", inverse_name="vehicle_id")
    repair_count = fields.Integer(compute="_compute_repair_count")

    def _compute_repair_count(self):
        for vehicle in self:
            vehicle.repair_count = 0

    @api.depends("brand", "model")
    def _compute_name(self):
        for rec in self:
            rec.name = f"{rec.brand or ''} {rec.model or ''}".strip()