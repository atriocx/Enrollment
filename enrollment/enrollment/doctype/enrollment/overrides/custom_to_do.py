import frappe
from frappe.desk.doctype.todo.todo import ToDo

class CustomToDo(ToDo):
    def on_update(self):
        
        super().on_update()
        
       
        frappe.logger().info("--- CustomToDo Ho gaya hai ---")