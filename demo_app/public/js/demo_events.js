// Listen for real-time events and show popup
// Listen for custom events and show popup
// Example: frappe.realtime.on('my_action', ...)
//update - 1

// List of custom action types to listen for
const customActionTypes = [
    'hello_world',
    "lead",
    "incoming_call"
    // Add more action types as needed
];

customActionTypes.forEach(function(actionType) {
    frappe.realtime.on(actionType, function(event) {
        frappe.msgprint(event.message);
    });
});
