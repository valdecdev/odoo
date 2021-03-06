# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# @author -  Fekete Mihai <feketemihai@gmail.com>
# Copyright (C) 2011 TOTAL PC SYSTEMS (http://www.www.erpsystems.ro).
# Copyright (C) 2009 (<http://www.filsystem.ro>)

from openerp.osv import fields, osv

class res_partner(osv.osv):
    _name = "res.partner"
    _inherit = "res.partner"
    _columns = {
        'nrc' : fields.char('NRC', help='Registration number at the Registry of Commerce'),
    }

    def _auto_init(self, cr, context=None):
        result = super(res_partner, self)._auto_init(cr, context=context)
        # Remove constrains for vat, nrc on "commercial entities" because is not mandatory by legislation
        # Even that VAT numbers are unique, the NRC field is not unique, and there are certain entities that
        # doesn't have a NRC number plus the formatting was changed few times, so we cannot have a base rule for
        # checking if available and emmited by the Ministry of Finance, only online on their website.
        
        cr.execute("""
            DROP INDEX IF EXISTS res_partner_vat_uniq_for_companies;
            DROP INDEX IF EXISTS res_partner_nrc_uniq_for_companies;
        """)
        return result
            
    def _commercial_fields(self, cr, uid, context=None):
        return super(res_partner, self)._commercial_fields(cr, uid, context=context) + ['nrc']
