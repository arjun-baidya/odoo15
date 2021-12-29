from odoo import fields, models, api
from datetime import datetime


class Rate(models.Model):
    _name = 'gold.rate'
    _description = "daily gold rate"

    name = fields.Char(string='Product Type :')
    rate = fields.Integer(string="gold rate")


class Order(models.Model):
    _name = 'order.order'
    _inherit = ['mail.thread', 'mail.activity.mixin', ]
    _description = "Order Receive Data"
    _rec_name = 'customer_name'

    # order_id = fields.Char(string="Code", rendomly=True)
    customer_name = fields.Char(string="Name", required=False)
    customer_mob = fields.Integer(string="Mobile No.", required=True)
    customer_address = fields.Char(string="Address", required=False, )
    product_type = fields.Selection(string="Product Type", selection=[('gold', 'Gold'), ('silver', 'Silver'), ],
                                    required=False, )
    product_type_id = fields.Many2one('gold.rate', string='Product Type :', change_default=True)
    gold_rate = fields.Integer(string="Gold Rate", required=True)
    order_date = fields.Datetime(string="Date", default=fields.datetime.now(), readonly="1")
    dele_date = fields.Datetime(string="Delivery Date", required=True)
    gold_orderline = fields.One2many(comodel_name="orderline.data", inverse_name="create_orderline",
                                     string="gold order", )
    paymentline = fields.One2many(comodel_name="paymentline.data", inverse_name="create_paymentline",
                                  string="gold payment", )

    @api.onchange('product_type_id')
    def onchange_product_type(self):
        if self.product_type_id:
            print(self.product_type_id)
            if self.product_type_id.rate:
                self.gold_rate = self.product_type_id.rate
                print(self.gold_rate)
        else:
            self.gold_rate = ''


class Order_Line(models.Model):
    _name = 'orderline.data'
    _description = "Oder details"

    product_name = fields.Selection(string="Product Name",
                                    selection=[('chain', 'Chain'), ('nackless', 'Nackless'), ('har', 'Har'),
                                               ('churi', 'Churi'), ('yearring', 'Year-Ring')], required=True, )
    weight = fields.Float(string="Weight", required=True)
    product_image = fields.Image(string="Image")
    product_quantity = fields.Integer(string="Quantity", required=True)
    making_cost = fields.Integer(string="Making cost", )
    gold_rate = fields.Many2one('gold.rate', string="Gold Rate", required=True, )
    sub_total_price = fields.Float(string="Sub Total Price", compute='gold_cost_count', store=True)
    create_orderline = fields.Many2one('order.order', string="Oder Line")

    @api.depends('weight', 'gold_rate')
    def gold_cost_count(self):
        for rec in self:
            rec.sub_total_price = ((rec.gold_rate / 96 * rec.weight) + rec.making_cost)


class PaymentLine(models.Model):
    _name = 'paymentline.data'
    # _inherits = {'orderline.data': 'sub_total_price'}
    _description = "Payment Details"

    price_id = fields.Many2one('orderline.data', )
    total_price = fields.Integer(string="Total Price")
    advance_payment = fields.Integer(string="Advance payment")
    total_due = fields.Float(string="Total Due")
    create_paymentline = fields.Many2one('order.order', string="Payment Line")

    # def call_func_c(self):
    #     return self.env["orderline.data"].gold_cost_count()

    # @api.depends('arjun')
    # def hello(self):
    #     for rec in self.price_id:
    #         rec.total_price = rec.sub_total_price

    # @api.depends('sub_total_price')
    # def hello(self):
    #     for rec in self:
    #         rec.total_price = self.env['orderline.data'].search([('sub_total_price', '=', 'origin')])
