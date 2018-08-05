# -*- coding: utf-8 -*-
# Copyright 2018 AitNasser Youssef.
# aitnasser@gmail.com
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
 
from odoo.exceptions import UserError
from odoo import fields, api, models, _

class AccountInvoice(models.Model):
	_inherit='account.invoice'

	@api.depends('amount_total')
	def get_amount_in_words(self):
		amount_in_words = self.currency_id.amount_to_text(self.amount_total)
		return amount_in_words