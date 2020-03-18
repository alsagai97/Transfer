from odoo import models, fields, api
from odoo.exceptions import Warning


class Transfer(models.Model):
    _inherit = 'stock.picking'

    @api.onchange('purchase.order.narration')
    def nar(self):
        if self.purchase.order.narration:
            self.narration = self.purchase.order.narration

    @api.onchange('product_id')
    def get(self):
        self.margin = self.product_id.standard_price

    narration = fields.Char(string='Narration', track_visibility="always", readonly=True, deafult=nar)
    x_narration = fields.Char(string='Narration', track_visibility="always", readonly=True)
    transfer_narration = fields.Char(string='Transfer Narration', track_visibility="always")
    received_by = fields.Char(string='Received By', track_visibility="always")
    reference = fields.Char(string='Reference', track_visibility="always")
    amount_to_be_paid = fields.Float(string='  Amount To Be Paid', digits=(14, 3), readonly=True,
                                     track_visibility="always")
    margin = fields.Float(string=' Margin', digits=(14, 3), readonly=True, compute='get')
    deliver_on_vehicle = fields.Many2one(string=' Deliver On Vehicle')
    slot_allocation_time = fields.Many2one(string=' Slot Allocation Time')
    sale_order_type = fields.Selection(string='Sale Order Type', readonly=True, default='cash_memo',
                                       selection=[('cash_memo', 'Cash Memo'), ('credit_sale', 'Credit Sale'),
                                                  ('paid_on_delivery', 'Paid on Delivery'),
                                                  ('advance_payment', 'Advance Payment')])
    journal_id = fields.Many2one('account.journal', string='Account Journal', readonly=True)
    partner_id = fields.Many2one(string='Contact', track_visibility="always")
    # currency_id = fields.Many2one('res.currency', string='Currency', readonly=True,
    #                               track_visibility="always")
    code = fields.Selection(related="picking_type_id.code")

# class Stock(models.Model):
#     _inherit = 'stock.picking.type'
#     code = fields.Selection([('incoming', 'Receipt'), ('outgoing', 'Delivery'), ('internal', 'Internal Transfer')],
#                             'Type of Operation', required=True, related='transfer_narration.code')
#     transfer_narration = fields.Char('Tracking_order', string='Transfer Narration', track_visibility="always",
#                                      related='code.transfer_narration')
