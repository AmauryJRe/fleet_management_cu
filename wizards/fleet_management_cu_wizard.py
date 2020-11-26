# -*- encoding: utf-8 -*-
"""Services module for handling unclear software list """
from odoo import fields, models, api


class CardDriver(models.Model):  
    _name = "fleet_management.wizard_driver"

    
    state = fields.Selection(
        [('acquired', 'Acquired'), ('maintenance', 'Maintenance'), ("broken", "Broken"), ('in_operation', 'Operational')], 'State')

    
    def new(self):
        data={}
        doc_ids = self.env['fleet.vehicle'].search([('state', '=', self.state)])
        data['doc_ids'] = self.env['fleet.vehicle'].search([('state', '=', self.state)])
        print(data)
        return self.env.ref('fleet_management_cu.report_by_state').report_action(doc_ids,data=data, config=False)
     