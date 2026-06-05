# Copyright (c) 2026, manas and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Student(Document):
    pass


@frappe.whitelist()
def get_latest_assignment(student):

    assignment = frappe.get_all(
        "Assignment",
        filters={"student": student},
        fields=["description"],
        order_by="creation desc",
        limit=1
    )

    if assignment:
        return assignment[0].description

    return None