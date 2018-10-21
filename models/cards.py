# coding=utf-8

from odoo import api, fields, models, _

class HrTravelSupportLoyaltyCard(models.Model):
    _name = "hr_travelsupport.loyaltycard"
    _description = 'Loyaltycard'
    employee_id = fields.Many2one('hr.employee', string='Employee',
                                  ondelete='cascade', index=True)
    name = fields.Selection(
        [
            'Finnair',
            'Lufthansa/Miles &amp; More',
            'Norwegian',
            'Scandic',
            'Avis',
            'Hertz',
            'S-Card',
        ],
        string='Card',
    )
    number = fields.Char('Number')

