# -*- coding: utf-8 -*-
{
    'name': "Get weather",

    'summary': """
        Get your client's location weather""",

    'description': """
        Bruh
    """,

    'author': "Vitaly Corp.",
    'website': "http://github.com/vitalya420",

    
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['crm'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
