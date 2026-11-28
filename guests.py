# Function to add a guest
def add_guest(event_data):

    print("\n----- Add Guest -----")

    # Existing guests, used to block duplicate names
    guests = event_data.get("guests", [])

    # Get guest name
    while True:
        name = input("Enter guest name: ").strip()

        if name == "":
            print("Guest name cannot be empty.")
        elif any(g["name"].lower() == name.lower() for g in guests):
            print("A guest with that name already exists. Please use a different name (for example, add a last initial).")
        else:
            break

    # Get guest contact information
    contact = input("Enter phone number or email: ").strip()

    # Create a dictionary for the guest
    guest = {
        "name": name,
        "contact": contact,
        "status": "pending",
        "attendance": ""
    }

    # Create the guest list if it does not exist
    if "guests" not in event_data:
        event_data["guests"] = []

    # Add the guest to the list
    event_data["guests"].append(guest)

    print("\nGuest added successfully!")


# Function to display the guest list
def display_guests(event_data):

    print("\n----- Guest List -----")

    guests = event_data.get("guests", [])

    if len(guests) == 0:
        print("No guests have been added.")
        return

    for number, guest in enumerate(guests, start=1):

        print("\nGuest", number)
        print("Name:", guest["name"])
        print("Contact:", guest["contact"])
        print("Status:", guest["status"])

        if guest["attendance"] != "":
            print("Attendance:", guest["attendance"])


# Function to update a guest's status
def update_guest_status(event_data):

    print("\n----- Update Guest Status -----")

    guests = event_data.get("guests", [])

    name = input("Enter the guest name: ").strip()

    for guest in guests:

        if guest["name"].lower() == name.lower():

            print("\n1. Confirmed")
            print("2. Declined")
            print("3. Pending")

            choice = input("Select the new status (1-3): ").strip()

            if choice == "1":
                guest["status"] = "confirmed"
            elif choice == "2":
                guest["status"] = "declined"
            elif choice == "3":
                guest["status"] = "pending"
            else:
                print("Invalid choice.")
                return

            print("\nGuest status updated successfully!")
            return

    print("Guest not found.")


# Function to remove a guest
def remove_guest(event_data):

    print("\n----- Remove Guest -----")

    guests = event_data.get("guests", [])

    name = input("Enter the guest name to remove: ").strip()

    for guest in guests:

        if guest["name"].lower() == name.lower():

            guests.remove(guest)

            print("\nGuest removed successfully!")
            return

    print("Guest not found.")


# Function to display guest statistics
def display_guest_statistics(event_data):

    print("\n----- Guest Statistics -----")

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
    print("Not Attending:", declined)


# Function to track actual guest attendance
def update_guest_attendance(event_data):

    print("\n----- Update Guest Attendance -----")

    guests = event_data.get("guests", [])

    name = input("Enter the guest name: ").strip()

    for guest in guests:

        if guest["name"].lower() == name.lower():

            print("\n1. Attended")
            print("2. Absent")

            choice = input("Select attendance (1-2): ").strip()

            if choice == "1":
                guest["attendance"] = "attended"
            elif choice == "2":
                guest["attendance"] = "absent"
            else:
                print("Invalid choice.")
                return

            print("\nGuest attendance updated successfully!")
            return

    print("Guest not found.")


# Main function called by main.py
def manage_guests(event_data):

    while True:

        print("\n========== GUEST MANAGEMENT ==========")
        print("1. Add Guest")
        print("2. Display Guest List")
        print("3. Update Guest Status")
        print("4. Remove Guest")
        print("5. Display Guest Statistics")
        print("6. Update Guest Attendance")
        print("7. Return to Main Menu")

        choice = input("\nEnter your choice (1-7): ").strip()

        if choice == "1":
            add_guest(event_data)

        elif choice == "2":
            display_guests(event_data)

        elif choice == "3":
            update_guest_status(event_data)

        elif choice == "4":
            remove_guest(event_data)

        elif choice == "5":
            display_guest_statistics(event_data)

        elif choice == "6":
            update_guest_attendance(event_data)

        elif choice == "7":
            print("Returning to Main Menu...")
            break

        else:
            print("Invalid choice. Please try again.")
