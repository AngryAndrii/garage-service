from odoo import models, fields, api


class GarageRepairLine(models.Model):
    _name = "garage.repair.line"
    _description = "Garage Repair Line"
    _order = "sequence, id"

    order_id = fields.Many2one("garage.repair.order", required=True, ondelete="cascade")
    service_type_id = fields.Many2one("garage.service.type", required=True)
    qty = fields.Float(default=1)
    price_unit = fields.Float()
    subtotal = fields.Float(compute="_compute_subtotal", store=True)
    currency_id = fields.Many2one(related="order_id.currency_id")
    sequence = fields.Integer(store=True)

    @api.depends("price_unit", "qty")
    def _compute_subtotal(self):
        for rec in self:
            rec.subtotal = rec.price_unit * rec.qty

# SQL-constraint: price_unit >= 0, qty > 0.
# Onchange: при виборі service_type_id → підставити price_unit з довідника.
