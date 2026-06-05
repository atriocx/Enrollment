frappe.ui.form.on("Assignment", {

    setup(frm) {

        frm.set_query("course", function() {
            return {
                query: "enrollment.enrollment.doctype.assignment.assignment.get_courses",
                filters: {
                    student: frm.doc.student,
                    semester: frm.doc.semester
                }
            };
        });

    },

    student: set_reference,
    course: set_reference,
    semester: set_reference

});

function set_reference(frm) {

    if (!(frm.doc.student && frm.doc.course && frm.doc.semester)) {
        return;
    }

    frappe.db.get_value(
        "Enrollment",
        {
            student: frm.doc.student,
            course: frm.doc.course,
            semester: frm.doc.semester
        },
        "name"
    ).then(r => {

        if (r.message && r.message.name) {
            frm.set_value("reference_type", "Enrollment");
            frm.set_value("reference_name", r.message.name);
        }

    });
}