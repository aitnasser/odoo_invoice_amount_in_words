# -*- coding: utf-8 -*-
# Copyright 2018 AitNasser Youssef.
# aitnasser@gmail.com
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


{
    'name': "invoice_amount_in_words",

    'summary': """
        Show invoice Amount in words.""",

    'description': """
         Show invoice Amount in words.
    """,

    'author': "Youssef AITNASSER",
     'email': "aitnasser@gmail.com",
    'website': "flexiapps.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Generic Modules/Accounting',
    
    'version': '11.0.1.0.1',

    "external_dependencies": {
        'python': ['num2words']
    },

    # any module necessary for this one to work correctly
    'depends': [ 'account'],

    # always loaded
    'data': [
        'views/report_invoice.xml'
    ],
    'installable': True,
    'auto_install': False,
}