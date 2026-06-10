// We will now write custom todo 

frappe.ui.form.on('ToDo', {
    refresh: function(frm) {
        // This fires when the ToDo document form is opened or reloaded
        console.log(" ToDo Form refreshed successfully!");
    },
    
    on_save: function(frm) {
        // This fires right when you hit the Save button
        console.log(" ToDo Form save triggered!");
    }
});