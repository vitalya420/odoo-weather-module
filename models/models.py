# -*- coding: utf-8 -*-

from odoo import models, fields, api
from .weather_api import WeatherAPI


class ResPartner(models.Model):
    _inherit = 'res.partner'

    weather = fields.Char(string="Weather", compute='_get_weather')

    @api.depends('city')
    def _get_weather(self):
        if self.city:
            wapi = WeatherAPI()
            res = wapi.get_weather(self.city)
            self.weather = "(" + wapi.formatted(res) + ")"
