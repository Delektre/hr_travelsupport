# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    _description = 'Employee'
    loyaltycard_ids = fields.One2many(
        'hr_travelsupport.loyaltycard',
        'employee_id',
        string='Loyaltycards'
    )
