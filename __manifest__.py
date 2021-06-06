# -*- coding: utf-8 -*-
{
    'name': "OpenWeatherMap",

    'summary': """
        Get your client's location get_weather""",

    'description': """
        View the get_weather in your clients' city
    """,

    'author': "Vitaly",
    'website': "http://github.com/vitalya420",


    'category': 'Productivity',
    'version': '0.2',
    'application': True,

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
