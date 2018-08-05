# -*- coding: utf-8 -*-
 
from odoo.exceptions import UserError
from odoo import fields, api, models, _

class AccountInvoice(models.Model):
	_inherit='account.invoice'

	#amount_in_words = fields.Char('Amount In Words', compute='_computeAmountInWords')

	@api.depends('amount_total')
	def get_amount_in_words(self):
		amount_in_words = self.currency_id.amount_to_text(self.amount_total)
		return amount_in_words