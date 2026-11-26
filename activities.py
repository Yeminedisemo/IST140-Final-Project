#imports the datetime module to make sure that the start time entered is a real time
from datetime import datetime


# Function to get a valid start time from the user
# The time is stored as HH:MM (24-hour) so that sorting by start time works correctly
def get_start_time(prompt):

    while True:

        start_time = input(prompt).strip()

        try:
            # Check that the time is a real time in 24-hour HH:MM format
            time = datetime.strptime(start_time, "%H:%M")

            # Return the time with a leading zero (for example 09:00)
            return time.strftime("%H:%M")

        except ValueError:
            print("Invalid time. Please enter the time as HH:MM (24-hour), for example 14:30.")


# Function to get a valid duration in minutes from the user
def get_duration(prompt):

    while True:

        minutes = input(prompt).strip()

        if minutes.isdecimal() and int(minutes) >= 1:
            return f"{int(minutes)} minutes"
        else:
            print("Invalid input. Please enter a whole number of minutes (1 or more).")


# Function to add an activity
def add_activity(event_data):

    print("\n----- Add Activity -----")

    # Get activity name
    while True:

        name = input("Enter activity name: ").strip()

        if name != "":
            break
        else:
            print("Activity name cannot be empty.")

    # Get the start time and duration
    start_time = get_start_time("Enter the start time (HH:MM, 24-hour): ")
    duration = get_duration("Enter the duration in minutes: ")

    # Get the description
    description = input("Enter a description of the activity: ").strip()

    # Create a dictionary to store the activity information
    activity = {
        "name": name,
        "start_time": start_time,
        "duration": duration,
        "description": description
    }

    # Create the activities list if it does not exist
    if "activities" not in event_data:
        event_data["activities"] = []

    # Add the activity to the list
    event_data["activities"].append(activity)

    print("\nActivity added successfully!")


# Function to display the activity schedule
def display_activities(event_data):

    print("\n----- Event Activities and Schedule -----")

    activities = event_data.get("activities", [])

    # Check if any activities have been added
    if len(activities) == 0:
        print("No activities have been added.")
        return

    # Sort activities according to start time
    sorted_activities = sorted(
        activities,
        key=lambda activity: activity["start_time"]
    )

    # Display each activity and its information
    for number, activity in enumerate(sorted_activities, start=1):

        print("\nActivity", number)
        print("Name:", activity["name"])
        print("Start Time:", activity["start_time"])
        print("Duration:", activity["duration"])
        print("Description:", activity["description"])


# Function to update an activity
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
                # If the user just presses enter, the original name is kept
                new_name = input(f"Enter the activity name ({activity['name']}): ").strip()
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


# Function to remove an activity
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
            print("Invalid choice. Please try again.")#activities.py
