import frappe


def execute():

    course = frappe.db.exists(
        "Courses",
        {"course_name": "DSA"}
    )

    if course:
        frappe.db.set_value(
            "Courses",
            course,
            "course_name",
            "C Foundation"
        )

        frappe.db.commit()