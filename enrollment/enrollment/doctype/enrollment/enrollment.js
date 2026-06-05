// Copyright (c) 2026, manas and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Enrollment", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on("Enrollment", {

    setup(frm) {

        frm.set_query("course", function() {

            return {
                filters: {
                    seats_available: [">", 0]
                }
            };
        });

    }
});