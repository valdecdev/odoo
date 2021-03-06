# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Purchase Management',
    'version': '1.1',
    'category': 'Purchase Management',
    'sequence': 19,
    'summary': 'Purchase Orders, Receipts, Vendor Bills',
    'description': """
Manage goods requirement by Purchase Orders easily
==================================================

Purchase management enables you to track your vendors' price quotations and convert them into purchase orders if necessary.
OpenERP has several methods of monitoring invoices and tracking the receipt of ordered goods. You can handle partial deliveries in OpenERP, so you can keep track of items that are still to be delivered in your orders, and you can issue reminders automatically.

OpenERP’s replenishment management rules enable the system to generate draft purchase orders automatically, or you can configure it to run a lean process driven entirely by current production needs.

Dashboard / Reports for Purchase Management will include:
---------------------------------------------------------
* Request for Quotations
* Purchase Orders Waiting Approval
* Monthly Purchases by Category
* Receipt Analysis
* Purchase Analysis
    """,
    'author': 'OpenERP SA',
    'website': 'https://www.odoo.com/page/purchase',
    'depends': ['stock_account', 'report', 'web_tip'],
    'data': [
        'security/purchase_security.xml',
        'security/ir.model.access.csv',
        'purchase_workflow.xml',
        'purchase_sequence.xml',
        'company_view.xml',
        'purchase_data.xml',
        'purchase_data.yml',
        'wizard/purchase_order_group_view.xml',
        'wizard/purchase_line_invoice_view.xml',
        'purchase_report.xml',
        'purchase_view.xml',
        'stock_view.xml',
        'partner_view.xml',
        'report/purchase_report_view.xml',
        'res_config_view.xml',
        'purchase_tip_data.xml',

        'views/report_purchaseorder.xml',
        'views/report_purchasequotation.xml',
    ],
    'test': [
        '../account/test/account_minimal_test.xml',
        'test/stock_valuation_account.xml',
        'test/ui/purchase_users.yml',
        'test/process/run_scheduler.yml',
        'test/fifo_price.yml',
        'test/fifo_returns.yml',
        # 'test/costmethodchange.yml',
        'test/process/cancel_order.yml',
        'test/process/rfq2order2done.yml',
        'test/process/generate_invoice_from_reception.yml',
        'test/process/merge_order.yml',
        'test/process/invoice_on_poline.yml',
        'test/ui/duplicate_order.yml',
        'test/ui/delete_order.yml',
        'test/average_price.yml',
        'test/anglo_saxon.yml',
        'test/anglo_saxon_avg_fifo.yml',
    ],
    'demo': [
        'purchase_order_demo.yml',
        'purchase_demo.xml',
        'purchase_stock_demo.yml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
