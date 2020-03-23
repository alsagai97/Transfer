{
    'name': 'Transfer_report : Transfer Out',
    'category': 'ticket',
    'summary': 'Transfer Report Customization',
    'version': '1.0',
    'description': """Customization of ticket module as per requirement.""",
    'depends': ['stock'],
    'data': [
        'data/report_paperformat.xml',
        'views/Transfer_out_report.xml',
        'views/Transfer_out_report_template.xml',

    ],
    'installable': True,
    'auto_install': False,
}
