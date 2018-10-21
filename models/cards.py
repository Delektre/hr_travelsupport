# coding=utf-8

from odoo import api, fields, models, _

class HrTravelSupportLoyaltyCard(models.Model):
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

