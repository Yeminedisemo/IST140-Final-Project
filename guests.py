
# Function to add a guest
def add_guest(event_data):

    print("\n========== ADD GUEST ==========")

    name = input("Enter guest name: ").strip()

    if name == "":
        print("Guest name cannot be empty.")
        return

    contact = input("Enter guest phone number or email: ").strip()

    if contact == "":
        print("Contact information cannot be empty.")
        return

    guest = {
        "name": name,
        "contact": contact,
        "status": "pending",
        "attendance": ""
    }

    if "guests" not in event_data:
        event_data["guests"] = []

    event_data["guests"].append(guest)

    print(name, "has been added successfully!")


# Function to display all guests
def display_guests(event_data):

    print("\n========== GUEST LIST ==========")

    guests = event_data.get("guests", [])

    if len(guests) == 0:
        print("No guests have been added.")
        return

    for number, guest in enumerate(guests, start=1):

        print("\nGuest", number)
        print("Name:", guest["name"])
        print("Contact:", guest["contact"])
        print("RSVP Status:", guest["status"])

        attendance = guest.get("attendance", "")

        if attendance != "":
            print("Attendance:", attendance)


# Function to update a guest's RSVP status
def update_guest_status(event_data):

    print("\n========== UPDATE GUEST STATUS ==========")

    guests = event_data.get("guests", [])

    name = input("Enter guest name: ").strip()

    for guest in guests:

        if guest["name"].lower() == name.lower():

            print("1. Confirmed")
            print("2. Pending")
            print("3. Declined")

            choice = input("Enter new status: ")

            if choice == "1":
                guest["status"] = "confirmed"
            elif choice == "2":
                guest["status"] = "pending"
            elif choice == "3":
                guest["status"] = "declined"
            else:
                print("Invalid choice.")
                return

            print("Guest status updated successfully!")
            return

    print("Guest not found.")


# Function to update actual guest attendance
def update_guest_attendance(event_data):

    print("\n========== UPDATE ATTENDANCE ==========")

    guests = event_data.get("guests", [])

    name = input("Enter guest name: ").strip()

    for guest in guests:

        if guest["name"].lower() == name.lower():

            print("1. Attended")
            print("2. Absent")

            choice = input("Enter attendance: ")

            if choice == "1":
                guest["attendance"] = "attended"
            elif choice == "2":
                guest["attendance"] = "absent"
            else:
                print("Invalid choice.")
                return

            print("Attendance updated successfully!")
            return

    print("Guest not found.")


# Function to remove a guest
def remove_guest(event_data):

    print("\n========== REMOVE GUEST ==========")

    guests = event_data.get("guests", [])

    name = input("Enter guest name to remove: ").strip()

    for guest in guests:

        if guest["name"].lower() == name.lower():

            guests.remove(guest)

            print(name, "has been removed.")
            return

    print("Guest not found.")


# Function to display guest statistics
def display_guest_statistics(event_data):

    print("\n========== GUEST STATISTICS ==========")

    guests = event_data.get("guests", [])

    confirmed = 0
    pending = 0
    declined = 0

    for guest in guests:

        status = guest["status"].lower()

        if status == "confirmed":
            confirmed += 1
        elif status == "pending":
            pending += 1
        elif status == "declined":
            declined += 1

    print("Total Guests:", len(guests))
    print("Confirmed:", confirmed)
    print("Pending:", pending)
    print("Declined:", declined)


# Main function called by main.py
def view_guest_management(event_data):

    while True:

        print("\n========== GUEST MANAGEMENT ==========")
        print("1. Add Guest")
        print("2. Display Guest List")
        print("3. Update Guest Status")
        print("4. Update Guest Attendance")
        print("5. Remove Guest")
        print("6. Display Guest Statistics")
        print("7. Return to Main Menu")

        choice = input("\nEnter your choice (1-7): ")

        if choice == "1":
            add_guest(event_data)

        elif choice == "2":
            display_guests(event_data)

        elif choice == "3":
            update_guest_status(event_data)

        elif choice == "4":
            update_guest_attendance(event_data)

        elif choice == "5":
            remove_guest(event_data)

        elif choice == "6":
            display_guest_statistics(event_data)

        elif choice == "7":
            print("Returning to Main Menu...")
            break

        else:
            print("Invalid choice. Please try again.")
