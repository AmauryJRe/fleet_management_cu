# -*- coding: utf-8 -*-

from odoo import models, fields, api
import math


class fleet_management_cu(models.Model):
    # _name = 'fleet_management_cu.fleet_management_cu'
    _inherit = 'fleet.vehicle'
    _sql_constraints = [
        ('inventory_number_unique', 'UNIQUE(inventory_number)',
         'Only one car can be assigned to the same Inventory number!'),
        ('engine_number_unique', 'UNIQUE(engine_number)',
         'Only one car can be assigned to the same Engine number!'),
        ('bodywork_number_unique', 'UNIQUE(bodywork_number)',
         'Only one car can be assigned to the same Bodywork number!'),
    ]

    driver_ids = fields.Many2many(comodel_name='res.partner', string='Driver')
    description = fields.Text('Description')
    max_speed = fields.Float('Max Speed in Km/h')
    weight = fields.Float('Weight in Kg')
    air_conditioning = fields.Boolean('It has air conditioning')
    inventory_number = fields.Char('Inventory Number')
    engine_number = fields.Char('Engine Number')
    bodywork_number = fields.Char('Bodywork Number')
    referals = fields.Integer('Referals')
    state = fields.Selection(
        [('acquired', 'Acquired'), ('maintenance', 'Maintenance'), ("broken", "Broken"), ('in_operation', 'In operation')], 'State', default='acquired',
        readonly=True, track_visibility='onchange')
    vehicle_type = fields.Selection([('regular_bus', 'Regular Bus'), ('tourism_bus', 'Tourism Bus'), (
        'tanker_truck', 'Tanker truck'), ('cargo_truk', 'Cargo truck')], string='Vehicle type')
    model = fields.Char(string='Model', related='model_id.name')
    brand = fields.Char(string='Brand', related='model_id.brand_id.name')
    emergency_windows = fields.Integer('Emergency windows')
    # doors = fields.Integer('Doors amount')
    # seats = fields.Integer('Seats amount')
    passengers = fields.Integer('Passengers amount')
    standing_passengers = fields.Integer(
        'Standing Passengers', compute='_compute_standing_passengers', store=True, readonly=True)
    reserved_seats = fields.Integer(
        'Reserved Seats', compute='_compute_reserved_seats', store=True, readonly=True)
    category = fields.Selection([('normal', 'Normal'), ('regular', 'Regular'), (
        'special', 'Special')], 'Category', default='normal')

    tv = fields.Boolean('Has TV')
    bathroom = fields.Boolean('Has bathroom')

    substance_type = fields.Selection([('flammable', 'Flammable'), ('no_flammable', 'No Flammable'), (
        'flammable_and_no_flammable', 'Flammable and No Flammable')], 'Substance type')
    max_load = fields.Integer('Max cargo')

    @api.onchange('seats', 'passengers')
    def _compute_standing_passengers(self):
        for record in self:
            record.standing_passengers = record.passengers - record.seats

    @api.onchange('seats')
    def _compute_reserved_seats(self):
        for record in self:
            record.reserved_seats = math.ceil(record.seats*0.12)

    def set_broken(self):
        self.state = 'broken'

    def set_maintenance(self):
        self.state = 'maintenance'

    def set_in_operation(self):
        self.state = 'in_operation'


# class fleet_partner_cu(models.Model):
#     # _name = 'fleet_management_cu.fleet_management_cu'
#     _inherit = 'res.partner'

#     vehicle_ids = fields.Many2many(comodel_name="fleet.vehicle")
