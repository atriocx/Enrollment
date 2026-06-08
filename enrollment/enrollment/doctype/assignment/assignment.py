import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc

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





@frappe.whitelist()

def make_todo(source_name, target_doc=None):

    def set_hardCoded_values(source, target):
        target.description = source.description
        target.assigned_by = source.teacher_name

    return get_mapped_doc(
        "Assignment",
        source_name,
        {
            "Assignment": {
                "doctype": "ToDo",
                "field_map": {
                    "name": "reference_name",
                    "doctype": "reference_type",
                },
                "field_no_map": ["date"],
            }
        },
        target_doc,
        set_hardCoded_values,
    )


@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def get_courses(doctype, txt, searchfield, start, page_len, filters):

    enrollments = frappe.get_all(
        "Enrollment",
        filters={
            "student": filters.get("student")
        },
        fields=["course"],
        distinct=True
    )

    return [[d.course] for d in enrollments]
@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def get_semesters(doctype, txt, searchfield, start, page_len, filters):

    enrollments = frappe.get_all(
        "Enrollment",
        filters={
            "student": filters.get("student"),
            "course": filters.get("course")
        },
        fields=["semester"],
        distinct=True
    )

    return [[d.semester] for d in enrollments]