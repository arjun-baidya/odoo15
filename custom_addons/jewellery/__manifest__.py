# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Jewellery ',
    'version': '13.0.1.0.0',
    'category': 'Gold',
    'description': """

    """,
    'summary': ' ',
    # 'website': 'https://www.odoo.com/page/survey',
    'depends': [
        'base',
        'mail',
    ],
    'data': [
        'views/order_view.xml',
        # 'views/payment_view.xml',
        'security/ir.model.access.csv',

    ],
    'installable': True,
    'application': True,
}
