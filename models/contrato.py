from odoo import fields, models
from datetime import datetime

class SaleOrder(models.Model):
    _inherit = "sale.order"

    contrato_externo = fields.Char(string = "Contrato externo")
    fecha_contrato = fields.Date(string = "Fecha de contrato", default = datetime.today())