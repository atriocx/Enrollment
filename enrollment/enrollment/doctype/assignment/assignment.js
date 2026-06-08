frappe.ui.form.on("Assignment", {

    setup(frm) {

        frm.set_query("course", function() {
            return {
                query: "enrollment.enrollment.doctype.assignment.assignment.get_courses",
                filters: {
                    student: frm.doc.student
                }
            };
        });

        frm.set_query("semester", function() {
            return {
                query: "enrollment.enrollment.doctype.assignment.assignment.get_semesters",
                filters: {
                    student: frm.doc.student,
                    course: frm.doc.course
                }
            };
        });

        frm.make_methods = {
            "ToDo": () => {
                frappe.model.open_mapped_doc({
                    method: "enrollment.enrollment.doctype.assignment.assignment.make_todo",
                    frm: frm
                });
            }
        };

    },

    student(frm) {
        frm.set_value("course", "");
        frm.set_value("semester", "");
    },

    course(frm) {
        frm.set_value("semester", "");
    }

});