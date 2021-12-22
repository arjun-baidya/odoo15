from odoo import fields, models, api
from datetime import datetime


class Payments(models.Model):
    _name = 'payment.data'
    _inherit = 'order.order'
    # _inherit = ['mail.thread', 'mail.activity.mixin', ]
    _description = "Order Receive Data"
    # _rec_name = 'customer_name'

    name = fields.Char(string="Name")




