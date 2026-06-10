# Copyright (c) 2026, manas and contributors
# For license information, please see license.txt

# Copyright (c) 2026, manas and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import nowdate


class StudentAttendance(Document):
    pass


def update_attendance_count():
    attendance_docs = frappe.get_all(
        "Student Attendance",
        filters={"attendance_date": nowdate()},
        pluck="name"
    )

    for docname in attendance_docs:
        doc = frappe.get_doc("Student Attendance", docname)

        for row in doc.student_attendance_forms:
            current_count = frappe.db.get_value(
                "Student",
                row.student,
                "attendance_count"
            ) or 0

            frappe.db.set_value(
                "Student",
                row.student,
                "attendance_count",
                current_count + 1
            )

    frappe.db.commit()