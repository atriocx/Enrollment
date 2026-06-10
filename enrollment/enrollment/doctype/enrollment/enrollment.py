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

    def on_submit(self):
        course = frappe.get_doc("Courses", self.course)

        if course.available_seats <= 0:
            frappe.throw("No seats available")

        course.available_seats = course.available_seats - 1
        course.save()
        
    def on_cancel(self):
        course = frappe.get_doc("Courses", self.course)
        course.available_seats = course.available_seats + 1
        course.save()