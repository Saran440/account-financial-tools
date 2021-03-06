# Copyright 2016 Akretion (Alexis de Lattre <alexis.delattre@akretion.com>)
# Copyright 2018 Tecnativa - Pedro M. Baeza
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    bank_receipt_offsetting_account = fields.Selection(
        readonly=False,
        related='company_id.bank_receipt_offsetting_account',
    )
    bank_receipt_transfer_account_id = fields.Many2one(
        related='company_id.bank_receipt_transfer_account_id',
        readonly=False,
    )
    bank_receipt_post_move = fields.Boolean(
        related='company_id.bank_receipt_post_move', readonly=False,
    )
