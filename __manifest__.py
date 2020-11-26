# -*- coding: utf-8 -*-
{
    'name': "Fleet Management.cu - Fleet Management",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','fleet'],

    # always loaded
    'data': [
        'security/fleet_management_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/menus.xml',
        'wizards/fleet_management_cu_wizard.xml',
        'reports/report_definition.xml',
        'reports/report_state.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable':True,
    'application':True,
}