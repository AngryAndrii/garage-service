from odoo import models, fields, api

GARAGE_ORDER_STATE = [
    ("draft", "Draft"),
    ("in_progress", "In Progress"),
    ("done", "Done"),
    ("cancelled", "Cancelled"),
]


class GarageRepairOrder(models.Model):
    _name = "garage.repair.order"
    _description = "Garage Repair Order"

    name = fields.Char(string="Name")
    vehicle_id = fields.Many2one("garage.vehicle", required=True, ondelete="restrict")
    mechanic_id = fields.Many2one("garage.mechanic")
    owner_id = fields.Many2one(related="vehicle_id.owner_id", store=True)
    state = fields.Selection(selection=GARAGE_ORDER_STATE, default="draft", copy=False)
    date_received = fields.Datetime(string="Date Received", default=lambda self: fields.Date.today())
    mileage_in = fields.Integer(string="Mileage")
    in_warranty = fields.Boolean(default=False)
    line_ids = fields.One2many("garage.repair.line", inverse_name="order_id")
    currency_id = fields.Many2one("res.currency", string="Currency", required=True)
    amount_total = fields.Monetary(compute="_compute_amount_total", store=True)

    # constrains date_delivered не раніше date_received не можна перевести в done, якщо line_ids порожній
    @api.depends("line_ids.subtotal")
    def _compute_amount_total(self):
        for rec in self:
            rec.amount_total = sum(rec.line_ids.mapped("subtotal"))
