#imports the datetime module to make sure that the date entered for the event is a real date
from datetime import datetime
#defines a function that will get information about the event
def get_event_info():
    print("\n-----Create Event-----")
    #creates an empty dictionary to store the information about the event
    event = {}
    #Validate the event name
    while True:
        #asks the user to enter an event name and removes the extra spaces
        event_name= input("Enter the event name: ").strip()
        #checks to see if the user entered a name for the event
        if event_name:
            #stores the event name in the event dictionary
            event["event_name"] = event_name
            break
        else:
            #will tell the user that the event needs a name
            print("Event name cannot be empty.")
    #Will allow the user to select the event type from a list of predefined types
    event_types = ["Birthday", "Wedding", "Graduation", "Corporate", "Anniversary", "Party", "Holiday", "Other"]
    print("\nSelect an event type:")
    #uses a for loop to show the different event types
    #uses start=1 so the loop doesnt start at 0
    for i, event_type in enumerate(event_types, start=1):
        print(f"{i}. {event_type}")
    #repeats while the user selects a valid event type
    while True:
        #asks the user to enter their choice and removes extra spaces
        choice = input("Enter your choice (1-8): ").strip()
        #checks to see if the user entered a valid choice
        if choice.isdigit() and 1 <= int(choice) <= len(event_types):
            #stores the selected event type in the event dictionary
            #converts the choice to an integer using int
            #subtracts 1 since the list positions being at an index of 0
            event["event_type"] = event_types[int(choice) - 1]
            break
        else:
            #will tell the user that the choice is invalid
            print("Invalid choice. Please enter a number from 1-8.")
    #Event date validation to ensure the date is in the correct format and is a real date
    while True:
        #asks the user to enter the date of the event and removes extra spaces
        event_date = input("Enter the date of the event (MM/DD/YYYY): ").strip()
        try:
            #tries to convert the entered date to a datetime object
            #and to see if it matches the mm/dd/yyyy format
            datetime.strptime(event_date, "%m/%d/%Y")
            #stores the valid date in the event dictionary
            event["event_date"] = event_date
            #breaks out of the loop once a valid date is entered
            break
        except ValueError:
            #will tell the user that the date format is invalid
            print("Invalid date format. Please enter the date as MM/DD/YYYY.")
    #aks the user to enter the location of the event and it adds it to the dictionary
    #removes spaces with strip
    event["event_location"] = input("Enter the location of the event: ").strip()
    #validates the expected number of guests
    #ensures the input is a digit and greater than or equal to 1
    while True:
        #asks the user to enter the expected number of guests and removes extra spaces
        guests = input("Enter the expected number of guests: ").strip()
        if guests.isdigit() and int(guests) >= 1:
            event["expected_guests"] = int(guests)
            break
        else:
            print("Invalid input. Please enter a number greater than or equal to 1.")
    #asks the user to enter a description of the event and saves it in the dictionary
    event["description"] = input("Enter a description of the event: ").strip()
    print("\nEvent information has been saved successfully!")
    #returns the dictionary
    return event
#defines a function that will display the information
#this information is about the event and is stored in the event dictionary
def display_event_info(event):
    #checks to see if the event dictionary is empty or not
    if not event:
        print("\nNo event information has been entered.")
        return
    #displays the event information from the dictionary
    print("\n-----Event Information-----")
    print(f"Event Name: {event['event_name']}")
    print(f"Event Type: {event['event_type']}")
    print(f"Event Date: {event['event_date']}")
    print(f"Event Location: {event['event_location']}")
    print(f"Expected Guests: {event['expected_guests']}")
    print(f"Description: {event['description']}")
#defines a function that will allow the user to update the event information
#this function will prompt the user to select which field to update and then update it in the event dictionary
def update_event_info(event):
    #checks to see if the dictionary is empty and if it is, prints a message and returns the dictionary
    if not event:
        print("\nNo event information has been entered.")
        return event
    #defines a list of valid event types for the user to choose from
    event_types = ["Birthday", "Wedding", "Graduation", "Corporate", "Anniversary", "Party", "Holiday", "Other"]
    #enters a loop to allow the user to update the event information repeatedly until they choose to return to the main menu
    while True:
        display_event_info(event)
        print("\n-----Update Event Information-----")
        print("1. Event Name")
        print("2. Event Type")
        print("3. Event Date")
        print("4. Event Location")
        print("5. Expected Guests")
        print("6. Description")
        print("7. Return to Main Menu")
        #prompts the user to enter their choice of which field to update and removes spaces using strip
        choice = input("\nWhat would you like to update? (1-7): ").strip()
        #handles the user's choice and updates the corresponding field in the event dictionary
        if choice == "1":
            #updates the event name in the event dictionary
            #if the user just presses enter without actually putting in anything then the program keeps the original event name
            event["event_name"] = input(f"Enter the event name ({event['event_name']}): ").strip() or event["event_name"]
        elif choice == "2":
            #updates the event type in the event dictionary
            print("\nSelect an event type:")
            #displays all the event types
            for i, event_type in enumerate(event_types, start=1):
                print(f"{i}. {event_type}")
            while True:
                #asks the user for their choice of event type
                type_choice = input("Enter your choice (1-8): ").strip()
                #checks if the user's input is a valid number within the range of event types
                if type_choice.isdigit() and 1 <= int(type_choice) <= len(event_types):
                    #updates the event type in the event dictionary
                    event["event_type"] = event_types[int(type_choice) - 1]
                    break
                else:
                    print("Invalid choice. Please enter a number from 1-8.")
        elif choice == "3":
            #updates the event date in the event dictionary
            while True:
                #asks the user to enter the new event date
                event_date = input(f"Enter the event date ({event['event_date']}): ").strip()
                if event_date == "":
                    #if the user just presses enter without actually putting in anything then the program keeps the original event date
                    break
                try:
                    #checks to see if the date is in the correct format
                    datetime.strptime(event_date, "%m/%d/%Y")
                    event["event_date"] = event_date
                    break
                except ValueError:
                    print("Invalid date format. Please enter the date as MM/DD/YYYY.")
        elif choice == "4":
            #updates the event location in the event dictionary
            event["event_location"] = input(f"Enter the event location ({event['event_location']}): ").strip() or event["event_location"]
        elif choice == "5":
            #updates the expected number of guests in the event dictionary
            while True:
                #asks the user to enter the expected number of guests
                guests = input(f"Enter the expected number of guests ({event['expected_guests']}): ").strip()
                #checks to see that the input contains only digits and is greater than or equal to 1
                if guests.isdigit() and int(guests) >= 1:
                    event["expected_guests"] = int(guests)
                    break
                else:
                    print("Invalid input. Please enter a number.")
        elif choice == "6":
            #updates the description of the event in the event dictionary
            event["description"] = input(f"Enter a description of the event ({event['description']}): ").strip() or event["description"]
        elif choice == "7":
            #exits the loop and returns to the main menu
            break
        else:
            print("Invalid choice. Please enter a number from 1-7.")
    #prints that the event information has been updated successfully
    print("\nEvent information has been updated successfully!")
    #returns the event dictionary
    return event