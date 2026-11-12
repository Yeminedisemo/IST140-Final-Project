#gets all the information from the 5 different modules
import overall_event_info
import guests
import finances
import activities
import summary_and_reviews
#stores the event data in a dictionary
#each module will have this dictionary
event_data = {}
#defines a function called main
def main():
    #allows this function to change the variable (event_data); which was something that was defined outside this function
    global event_data
    #starts the loop and shows the user what their options are
    while True:
        print("\n================================")
        print("          EVENT MANAGER")
        print("==================================")
        print("1. Create the Event and Enter Details")
        print("2. Display Event Information")
        print("3. Update Event Information")
        print("4. Manage Guests")
        print("5. Manage Event Finances")
        print("6. Manage Activities")
        print("7. View Event Summary and Reviews")
        print("8. Exit")
        #asks the user for their choice and removes extra spaces using strip
        choice = input("\nEnter your choice (1-8): ").strip()
        #Create the event and its relating information
        #Creates a new event and gets information for that event
        if choice == "1":
            #calls the function from the overall_event_info module and stores the results in the event_data dictionary
            event_data = overall_event_info.get_event_info()
        #displays the event information if it exists
        elif choice == "2":
            if event_data:
                #calls the function from the overall_event_info module to display the event information
                overall_event_info.display_event_info(event_data)
            else:
                print("No event information available. Please create an event first.")
        #updates the event information if it exists
        elif choice == "3":
            if event_data:
                #calls the function from the overall_event_info module to update the event information
                event_data = overall_event_info.update_event_info(event_data)
            else:
                print("No event information available. Please create an event first.")
        elif choice == "4":
            #manages the guests for the event if it exists
            if event_data:
                #calls the function from the guests module to manage the guests for the event
                guests.manage_guests(event_data)
            else:
                print("No event information available. Please create an event first.")
        elif choice == "5":
            #manages the event finances if the event exists
            if event_data:
                #calls the function from the finances module to manage the event finances
                finances.manage_finances(event_data)
            else:
                print("No event information available. Please create an event first.")
        elif choice == "6":
            #manages the activities for the event if it exists
            if event_data:
                #calls the function from the activities module to manage the activities for the event
                activities.manage_activities(event_data)
            else:
                print("No event information available. Please create an event first.")
        elif choice == "7":
            #views the event summary and reviews if the event exists
            if event_data:
                #calls the function from the summary_and_reviews module to view the event summary and reviews
                summary_and_reviews.view_summary_and_reviews(event_data)
            else:
                print("No event information available. Please create an event first.")
        elif choice == "8":
            #breaks the loop and exits the program
            print("Exiting Event Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1-8.")
#checks whether it this python file is being run directly
#if this is the file that is being run then it calls the main function to start the program
#this ensures that this function won't run unless it is being run directly
if __name__ == "__main__":
    main()