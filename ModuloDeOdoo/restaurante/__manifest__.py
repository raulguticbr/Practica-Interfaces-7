# -*- coding: utf-8 -*-
{
    'name': "restaurante",

    'summary': """Modulo de platos y menus""",

    'description': """
        Módulo para manejar:
        -platos
        -menus
    """,

    'author': "Ale",
    'website': "http://www.repositoriocompartido.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/templates.xml',
        'views/plato.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
