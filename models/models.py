# -*- coding: utf-8 -*-

from odoo import models, fields, api
from .weather_api import WeatherAPI


class ResPartner(models.Model):
    _inherit = 'res.partner'

    weather = fields.Char(string="Weather", compute='_get_weather')

    @api.depends('city')
    def _get_weather(self):
        if self.city:
            weather_api = WeatherAPI()
            res = weather_api.get_weather(self.city)
            self.weather = "(" + weather_api.formatted(res) + ")\n"
