import frappe
from frappe.model.document import Document


class Assignment(Document):

    def validate(self):

        enrollment_exists = frappe.db.exists(
            "Enrollment",
            {
                "student": self.student,
                "course": self.course,
                "semester": self.semester
            }
        )

        if not enrollment_exists:
            frappe.throw(
                "Selected student is not enrolled in the selected course and semester."
            )

    def after_insert(self):

        frappe.get_doc({
            "doctype": "ToDo",
            "description": f"Complete Assignment {self.name}",
            "status": "Open",
            "allocated_to": frappe.session.user
        }).insert(ignore_permissions=True)


@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def get_courses(doctype, txt, searchfield, start, page_len, filters):

    enrollments = frappe.get_all(
        "Enrollment",
        filters={
            "student": filters.get("student"),
            "semester": filters.get("semester")
        },
        fields=["course"]
    )

    return [[d.course] for d in enrollments]