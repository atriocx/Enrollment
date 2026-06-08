import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.model.utils.rename_field import rename_field
from frappe.utils import add_years, today


def execute():
    rename_dsa_course()
    rename_student_field()
    add_status_field()
    insert_courses()
    update_student_status()


def rename_dsa_course():
    """
    Rename Course document DSA -> C Foundation
    and update all linked Enrollment records automatically.
    """

    if frappe.db.exists("Courses", "DSA"):
        frappe.rename_doc(
            "Courses",
            "DSA",
            "C Foundation",
            force=True,
            merge=False
        )


def rename_student_field():
    """
    Rename first_name -> student_name
    """

    meta = frappe.get_meta("Student")

    if meta.has_field("first_name") and not meta.has_field("student_name"):
        rename_field(
            "Student",
            "first_name",
            "student_name"
        )


def add_status_field():

    if not frappe.db.exists(
        "DocField",
        {
            "parent": "Student",
            "fieldname": "status"
        }
    ):
        create_custom_fields(
            {
                "Student": [
                    {
                        "fieldname": "status",
                        "label": "Status",
                        "fieldtype": "Select",
                        "options": "Active\nNot Active",
                        "default": "Not Active",
                        "insert_after": "grade"
                    }
                ]
            }
        )


def insert_courses():

    courses = [
        {
            "course_name": "Python Programming",
            "credits": 4,
            "department": "Computer Science",
            "course_fee": 5000,
            "seats_available": 40
        },
        {
            "course_name": "Data Structures",
            "credits": 3,
            "department": "Computer Science",
            "course_fee": 4500,
            "seats_available": 35
        },
        {
            "course_name": "Database Systems",
            "credits": 4,
            "department": "Computer Science",
            "course_fee": 5500,
            "seats_available": 30
        },
        {
            "course_name": "Operating Systems",
            "credits": 4,
            "department": "Computer Science",
            "course_fee": 6000,
            "seats_available": 25
        },
        {
            "course_name": "Machine Learning",
            "credits": 5,
            "department": "AI",
            "course_fee": 8000,
            "seats_available": 20
        }
    ]

    for course in courses:

        if not frappe.db.exists(
            "Courses",
            {"course_name": course["course_name"]}
        ):
            frappe.get_doc(
                {
                    "doctype": "Courses",
                    **course
                }
            ).insert(ignore_permissions=True)


def update_student_status():

    last_year = add_years(today(), -1)

    enrollments = frappe.get_all(
        "Enrollment",
        filters={
            "enrollment_date": [">=", last_year]
        },
        fields=["student"]
    )

    for enrollment in enrollments:

        frappe.db.set_value(
            "Student",
            enrollment.student,
            "status",
            "Active"
        )

    frappe.db.commit()