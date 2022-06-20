{
    'name': 'Manejo de contratos',
    'version': '1.0.0',
    'category': 'Contratos',
    'summary': 'Un módulo de contratos',
    'description': """Un módulo que gestiona tus contratos""",
    'application': True,
    'sequence': 0,
    'depends': [
        'sale'
    ],
    'data': [
        'views/view.xml',
        'reports/contract_report.xml'
    ]
}