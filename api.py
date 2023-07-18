import requests

# Biometric Device API endpoint for employee punches
biometric_device_api = 'https://biometric-device-api.com/punch'

# Odoo API endpoint for creating and updating attendance records
odoo_api = 'https://your-odoo-instance.com/api/attendance'

def punch_event_handler(employee_id, check_time):
    # Step 1: Handle employee punch event from the biometric device
    # This function is triggered when the biometric device receives a punch from an employee
    # It captures the employee ID and check-in/out time

    if check_time == 'check_in':
        # Step 2: Create attendance record in Odoo for employee check-in
        attendance_data = {
            'employee_id': employee_id,
            'check_in': check_time,
        }
        response = requests.post(odoo_api, json=attendance_data)
        if response.status_code == 201:
            print("Attendance record created for employee check-in.")
        else:
            print("Failed to create attendance record for employee check-in.")

    elif check_time == 'check_out':
        # Step 3: Update attendance record in Odoo for employee check-out
        attendance_data = {
            'employee_id': employee_id,
            'check_out': check_time,
        }
        response = requests.put(odoo_api, json=attendance_data)
        if response.status_code == 200:
            print("Attendance record updated for employee check-out.")
        else:
            print("Failed to update attendance record for employee check-out.")

# Simulating a punch event from the biometric device
employee_id = 123
check_time = 'check_in'

punch_event_handler(employee_id, check_time)
