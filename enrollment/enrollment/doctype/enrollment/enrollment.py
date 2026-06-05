# Copyright (c) 2026, manas and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Enrollment(Document):

    def after_insert(self):
        frappe.get_doc({
            "doctype": "ToDo",
            "description": f"Student: {self.student}"
        }).insert(ignore_permissions=True)