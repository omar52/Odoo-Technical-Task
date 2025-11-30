{
    'name': 'Odoo Technical Task',
    'version': '17.0.1.0.0',
    'summary': 'Implementation of Customer Regionalization and Sales Credit Limit management.',
    'author': 'Omar',
    'website': '',
    'category': 'Sales',
    'depends': ['base', 'sale_management', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'security/main_security.xml',
        'views/main_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}