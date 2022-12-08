{
    'name': 'Website Reorder',
    'version': '16.0.1.0',
    'sequence': -100,
    'category': 'Website Reorder',
    'summary': 'Reorder The Sale Orders',
    'application': True,
    'depends': [
        'base',
        'sale',
        'website',
    ],
    'data': [
        'views/sale_reorder.xml'
    ],
    'assets': {
        'web.assets_frontend': [
            'website_reorder/static/src/js/website_portal_button.js'

        ],
    },

}
