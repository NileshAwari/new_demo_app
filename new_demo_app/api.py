import frappe

@frappe.whitelist()
def hello_world():
    print("hello_world")
    return "hello_world"

@frappe.whitelist()
def emit_custom_event(action_type, message, user=None):
    event_data = {
        "action_type": action_type,
        "message": message,
        "user": user
    }
    frappe.publish_realtime(
        event=action_type,  # event name is dynamic
        message=event_data,
        user=user  # if user is None, event goes to all users
    )
    return "Event emitted"
