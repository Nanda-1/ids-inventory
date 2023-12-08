# -*- coding: utf-8 -*-

from odoo import models, fields, api
from collections import OrderedDict
from datetime import datetime


class InheritStockPicking(models.Model):
    _inherit = 'stock.picking'
    _description = 'ids_inherit_inventory.ids_inherit_inventory'

    def write_roman(num):

        roman = OrderedDict()
        roman[1000] = "M"
        roman[900] = "CM"
        roman[500] = "D"
        roman[400] = "CD"
        roman[100] = "C"
        roman[90] = "XC"
        roman[50] = "L"
        roman[40] = "XL"
        roman[10] = "X"
        roman[9] = "IX"
        roman[5] = "V"
        roman[4] = "IV"
        roman[1] = "I"

        def roman_num(num):
            for r in roman.keys():
                x, y = divmod(num, r)
                yield roman[r] * x
                num -= (r * x)
                if num <= 0:
                    break

        return "".join([a for a in roman_num(num)])


    @api.model_create_multi
    def create(self, vals_list):
        current_month = datetime.now().month
        current_year = datetime.now().year
        scheduled_dates = []
        for vals in vals_list:
            defaults = self.default_get(['name', 'picking_type_id'])
            picking_type = self.env['stock.picking.type'].browse(vals.get('picking_type_id', defaults.get('picking_type_id')))
            if vals.get('name', '/') == '/' and defaults.get('name', '/') == '/' and vals.get('picking_type_id', defaults.get('picking_type_id')):
                if picking_type.sequence_id:
                    partner_id = vals.get('partner_id', False)
                    partner = self.env['res.partner'].browse(partner_id) if partner_id else False
                    partner_name = partner.singkatan if partner else ''

                    roman = InheritStockPicking.write_roman(current_month)
                    vals['name'] = picking_type.sequence_id.next_by_id() + '/' + str(partner_name) + '/' + str(roman) + '/' + str(current_year) 


            # make sure to write `schedule_date` *after* the `stock.move` creation in
            # order to get a determinist execution of `_set_scheduled_date`
            scheduled_dates.append(vals.pop('scheduled_date', False))

        pickings = super().create(vals_list)

        for picking, scheduled_date in zip(pickings, scheduled_dates):
            if scheduled_date:
                picking.with_context(mail_notrack=True).write({'scheduled_date': scheduled_date})
        pickings._autoconfirm_picking()

        for picking, vals in zip(pickings, vals_list):
            # set partner as follower
            if vals.get('partner_id'):
                if picking.location_id.usage == 'supplier' or picking.location_dest_id.usage == 'customer':
                    picking.message_subscribe([vals.get('partner_id')])
            if vals.get('picking_type_id'):
                for move in picking.move_ids:
                    if not move.description_picking:
                        move.description_picking = move.product_id.with_context(lang=move._get_lang())._get_description(move.picking_id.picking_type_id)
        return pickings

class InheritContact(models.Model):
    _inherit = 'res.partner'
    
    singkatan = fields.Char('singkatan')

