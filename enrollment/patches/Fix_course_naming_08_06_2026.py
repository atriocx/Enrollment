import frappe

def execute():
    if frappe.db.exists("Courses", "data structures"):
        frappe.rename_doc(
            "Courses",
            "data structures",
            "C Foundation Advanced", # Changed name to avoid database duplication conflict
            force=True
        )