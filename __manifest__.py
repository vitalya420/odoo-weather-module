# -*- coding: utf-8 -*-
{
    'name': "Get weather",

    'summary': """
        Get your client's location weather""",

    'description': """
        View the weather in your clients' city
    """,

    'author': "Vitaly Corp.",
    'website': "http://github.com/vitalya420",

    
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['crm'],


    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
