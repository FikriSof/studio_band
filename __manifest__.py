# -*- coding: utf-8 -*-
{
    'name': "studio_band",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services',
    'version': '0.1',
    'application':True,

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml',
        'views/studiomusik.xml',
        'views/alatmusik.xml',
        'views/paketband.xml',
        'views/order.xml',
        'views/pegawai.xml',
        'views/customer.xml',
        'views/orderselesai.xml',
        'report/report.xml',
        'report/order_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
