from odoo import models, fields


class GarageRepairOrder(models.Model):
    _name = "garage.repair.order"
    _description = "Garage Repair Order"

    name = fields.Char(string="Name")
    vehicle_id = fields.Many2one("garage.vehicle", required=True, ondelete="restrict")
    # mechanic_id = fields.Many2one("garage.mechanic")
    owner_id = fields.Many2one(related="vehicle_id.owner_id", store=True)
    state = fields.Selection([
        ("draft", "Draft"),
        ("in_progress", "In Progress"),
        ("done", "Done"),
        ("cancelled", "Cancelled"),
    ], default="draft", copy=False)
    date_received = fields.Datetime(string="Date Received", default=lambda self: fields.Date.today())
    mileage_in = fields.Integer(string="Mileage")
    in_warranty =fields.Boolean(default=False)
    # line_ids = fields.One2many("garage.repair.line", inverse="garage.order_id")
    currency_id = fields.Many2one("res.currency", string="Currency", required=True)
    # amount_total = fields.Monetary(compute="_compute_amount_total", store=True)
    amount_untaxed_display = fields.Monetary(compute="_compute_untaxed_display", store=False)

    def _compute_untaxed_display(self):
        total = 0
        for el in self:
            total += el

    # constrains date_delivered не раніше date_received не можна перевести в done, якщо line_ids порожній

