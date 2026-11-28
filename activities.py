from datetime import datetime


# Gets a valid start time (24-hour HH:MM)
def get_start_time(prompt):

    while True:

        start_time = input(prompt).strip()

        try:
            time = datetime.strptime(start_time, "%H:%M")
            return time.strftime("%H:%M")

        except ValueError:
            print("Invalid time. Please enter the time as HH:MM, for example 14:30.")


# Gets a valid duration in minutes
def get_duration(prompt):

    while True:

        minutes = input(prompt).strip()

        if minutes.isdecimal() and int(minutes) >= 1:
            return f"{int(minutes)} minutes"
        else:
            print("Invalid input. Please enter a whole number of minutes.")


# Adds an activity
def add_activity(event_data):

    print("\n----- Add Activity -----")

    # Existing activities, used to block duplicate names
    activities = event_data.get("activities", [])

    while True:

        name = input("Enter activity name: ").strip()

        if name == "":
            print("Activity name cannot be empty.")
        elif any(a["name"].lower() == name.lower() for a in activities):
            print("An activity with that name already exists. Please use a different name.")
        else:
            break

    start_time = get_start_time("Enter the start time (HH:MM, 24-hour): ")
    duration = get_duration("Enter the duration in minutes: ")
    description = input("Enter a description of the activity: ").strip()

    activity = {
        "name": name,
        "start_time": start_time,
        "duration": duration,
        "description": description
    }

    if "activities" not in event_data:
        event_data["activities"] = []

    event_data["activities"].append(activity)

    print("\nActivity added successfully!")


# Displays the activities sorted by start time
def display_activities(event_data):

    print("\n----- Event Activities and Schedule -----")

    activities = event_data.get("activities", [])

    if len(activities) == 0:
        print("No activities have been added.")
        return

    sorted_activities = sorted(
        activities,
        key=lambda activity: activity["start_time"]
    )

    for number, activity in enumerate(sorted_activities, start=1):

        print("\nActivity", number)
        print("Name:", activity["name"])
        print("Start Time:", activity["start_time"])
        print("Duration:", activity["duration"])
        print("Description:", activity["description"])


# Updates an activity
def update_activity(event_data):

    print("\n----- Update Activity -----")

    activities = event_data.get("activities", [])

    name = input("Enter the name of the activity to update: ").strip()

    for activity in activities:

        if activity["name"].lower() == name.lower():

            print("\n1. Name")
            print("2. Start Time")
            print("3. Duration")
            print("4. Description")

            choice = input("What would you like to update? (1-4): ").strip()

            if choice == "1":
                new_name = input(f"Enter the activity name ({activity['name']}): ").strip()
                if any(other is not activity and other["name"].lower() == new_name.lower()
                       for other in activities):
                    print("Another activity already has that name. Name not changed.")
                    return
                if new_name != "":
                    activity["name"] = new_name

            elif choice == "2":
                activity["start_time"] = get_start_time(
                    f"Enter the start time ({activity['start_time']}): "
                )

            elif choice == "3":
                activity["duration"] = get_duration(
                    f"Enter the duration in minutes ({activity['duration']}): "
                )

            elif choice == "4":
                new_description = input(
                    f"Enter the description ({activity['description']}): "
                ).strip()
                if new_description != "":
                    activity["description"] = new_description

            else:
                print("Invalid choice.")
                return

            print("\nActivity updated successfully!")
            return

    print("Activity not found.")


# Removes an activity
def remove_activity(event_data):

    print("\n----- Remove Activity -----")

    activities = event_data.get("activities", [])

    name = input("Enter the name of the activity to remove: ").strip()

    for activity in activities:

        if activity["name"].lower() == name.lower():

            activities.remove(activity)

            print("\nActivity removed successfully!")
            return

    print("Activity not found.")


# Main function called by main.py
def manage_activities(event_data):

    while True:

        print("\n========== ACTIVITY MANAGEMENT ==========")
        print("1. Add Activity")
        print("2. Display Activity Schedule")
        print("3. Update Activity")
        print("4. Remove Activity")
        print("5. Return to Main Menu")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            add_activity(event_data)

        elif choice == "2":
            display_activities(event_data)

        elif choice == "3":
            update_activity(event_data)

        elif choice == "4":
            remove_activity(event_data)

        elif choice == "5":
            print("Returning to Main Menu...")
            break

        else:
            print("Invalid choice. Please try again.")
