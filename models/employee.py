# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class HrEmployeeTravel(models.Model):
    _inherit = 'hr.employee'
    loyaltycard_ids = fields.One2Many(
        'hr_travelsupport.loyaltycard',
        string='Loyaltycards',
    )

