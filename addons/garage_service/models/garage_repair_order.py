from odoo import models, fields, api
from odoo.exceptions import ValidationError

GARAGE_ORDER_STATE = [
    ("draft", "Draft"),
    ("in_progress", "In Progress"),
    ("done", "Done"),
    ("cancelled", "Cancelled"),
]


class GarageRepairOrder(models.Model):
    _name = "garage.repair.order"
    _description = "Garage Repair Order"
    _order = "date_received, state"

    name = fields.Char(string="Name")
    vehicle_id = fields.Many2one("garage.vehicle", required=True, ondelete="restrict")
    mechanic_id = fields.Many2one("garage.mechanic")
    owner_id = fields.Many2one(related="vehicle_id.owner_id", store=True)
    state = fields.Selection(selection=GARAGE_ORDER_STATE, default="draft", copy=False)
    date_received = fields.Date(string="Date Received", default=lambda self: fields.Date.today())
    date_delivered = fields.Date()
    mileage_in = fields.Integer(string="Mileage")
    in_warranty = fields.Boolean(default=False)
    line_ids = fields.One2many("garage.repair.line", inverse_name="order_id")
    currency_id = fields.Many2one("res.currency", string="Currency", required=True)
    amount_total = fields.Monetary(compute="_compute_amount_total", store=True)

    @api.depends("line_ids.subtotal")
    def _compute_amount_total(self):
        for rec in self:
            rec.amount_total = sum(rec.line_ids.mapped("subtotal"))

    @api.constrains("date_delivered", "date_received")
    def _check_date_delivered(self):
        for order in self:
            if order.date_delivered and order.date_received:
                if order.date_delivered < order.date_received:
                    raise ValidationError("Date delivered must be after date_received")

    @api.constrains("state", "line_ids")
    def _check_lines_on_done(self):
        for order in self:
            if order.state == "done" and not order.line_ids:
                raise ValidationError("Line ids cannot be empty for line ending")

    def button_in_progress(self):
        self.write({'state': "in_progress"})

    def button_cancel(self):
        self.write({'state': "cancelled"})