# coding=utf-8

from odoo import api, fields, models, _

class HrTravelSupportLoyaltyCard(models.Model):
    _name = "hr_travelsupport.loyaltycard"
    _description = 'Loyaltycard'
    _inherit = ['mail.thread']

    name = fields.Selection(
        [
            'Finnair',
            'Lufthansa/Miles &amp; More',
            'SAS',
            'Norwegian',
            'Scandic',
            'Avis',
            'Hertz',
            'S-Card',
        ],
        string='Card',
    )

    employee_id = fields.Many2one('hr.employee', string='Employee',
                                  ondelete='cascade', index=True)
    
    number = fields.Char('Number')
    date_end = fields.Date('End Date', default=None)
