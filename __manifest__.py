# -*- coding: utf-8 -*-
{
    'name': "ids_inherit_inventory",

    'summary': """
        IBS Inventory """,

    'description': """
        To Create Report for IBS
    """,
    "license": "LGPL-3",
    'author': "Nanda Soe",
    'website': "https://ib-synergy.co.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock', 'contacts'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
        
        'views/inherit_res_partner.xml',
        'views/inherit_stock_picking.xml',
        
        'report/report_stock_picking.xml',
        'report/inherit_stock_deliveryslip.xml',
        'report/report_deliveryslip_new.xml',
        # 'report/stock_report_views.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}
