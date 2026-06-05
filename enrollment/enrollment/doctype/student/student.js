// Copyright (c) 2026, manas and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Student", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on("Student", {
    refresh(frm) {

        if (!frm.is_new()) {

            frm.add_custom_button("Get Assignment Details", function() {

                frappe.call({
                    method: "enrollment.enrollment.doctype.student.student.get_latest_assignment",
                    args: {
                        student: frm.doc.name
                    },
                    callback: function(r) {

                        if (r.message) {

                            frappe.msgprint({
                                title: "Latest Assignment",
                                message: r.message,
                                indicator: "blue"
                            });

                        } else {
                            frappe.msgprint("No assignment found");
                        }
                    }
                });

            });

        }
    }
});