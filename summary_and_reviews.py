
# Function to display the complete event summary
def display_summary(event_data):

    print("\n========== EVENT SUMMARY ==========")

    # Display event information
    print("\n----- Event Information -----")
    print("Event Name:", event_data.get("event_name", "Not entered"))
    print("Event Type:", event_data.get("event_type", "Not entered"))
    print("Event Date:", event_data.get("event_date", "Not entered"))
    print("Event Location:", event_data.get("event_location", "Not entered"))

    # Get guest information
    guests = event_data.get("guests", [])

    # Count guest attendance
    attending = 0
    pending = 0
    not_attending = 0
    came = 0
    did_not_come = 0

    for guest in guests:

        status = guest["status"].lower()

        if status == "confirmed":
            attending += 1
        elif status == "pending":
            pending += 1
        elif status == "declined":
            not_attending += 1

        attendance = guest.get("attendance", "").lower()

        if attendance == "attended":
            came += 1
        elif attendance == "absent":
            did_not_come += 1

    # Display guest information
    print("\n----- Guest Information -----")
    print("Total Guests:", len(guests))
    print("Guests Confirmed:", attending)
    print("Guests Pending:", pending)
    print("Guests Not Attending:", not_attending)
    print("Guests Who Came:", came)
    print("Guests Who Did Not Come:", did_not_come)

    # Get financial information
    budget = event_data.get("budget", 0)
    expenses = event_data.get("expenses", [])

    total_expenses = 0

    # Display expenses
    print("\n----- Event Expenses -----")

    for expense in expenses:

        print("Expense:", expense["name"])
        print("Category:", expense["category"])
        print("Cost: $", expense["cost"])

        total_expenses += float(expense["cost"])

    # Calculate remaining budget
    remaining_budget = float(budget) - total_expenses

    # Display financial summary
    print("\n----- Financial Summary -----")
    print(f"Original Budget: ${float(budget):.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Remaining Budget: ${remaining_budget:.2f}")

    if remaining_budget < 0:
        print("WARNING: You have exceeded your budget!")
    else:
        print("You are within your budget.")

    # Get activity information
    activities = event_data.get("activities", [])

    # Display activities
    print("\n----- Event Activities and Schedule -----")

    # Sort activities according to start time
    activities = sorted(
        activities,
        key=lambda activity: activity["start_time"]
    )

    if len(activities) == 0:
        print("No activities have been added.")

    else:
        for number, activity in enumerate(activities, start=1):

            print("\nActivity", number)
            print("Name:", activity["name"])
            print("Start Time:", activity["start_time"])
            print("Duration:", activity["duration"])
            print("Description:", activity["description"])


# Function to collect guest reviews
def add_review(event_data):

    print("\n========== SUBMIT EVENT REVIEW ==========")

    # Create a reviews list if one does not exist
    if "reviews" not in event_data:
        event_data["reviews"] = []

    # Ask for guest name
    while True:

        name = input("Enter your name: ").strip()

        if name != "":
            break
        else:
            print("Name cannot be empty.")

    # Ask for rating
    while True:

        rating = input("Rate the event out of 5 stars: ")

        if rating.isdigit() and 1 <= int(rating) <= 5:
            rating = int(rating)
            break
        else:
            print("Please enter a rating between 1 and 5.")

    # Ask for review information
    favorite = input("What was your favorite part of the event? ")
    least_favorite = input("What was your least favorite part? ")
    recommendations = input("What recommendations do you have? ")
    organizer_opinion = input(
        "What is your opinion on how the event was organized? "
    )

    # Store review information in a dictionary
    review = {
        "name": name,
        "rating": rating,
        "favorite": favorite,
        "least_favorite": least_favorite,
        "recommendations": recommendations,
        "organizer_opinion": organizer_opinion
    }

    # Add the review to the reviews list
    event_data["reviews"].append(review)

    print("\nYour review has been saved successfully!")


# Function to display reviews from highest rating to lowest
def display_reviews(event_data):

    print("\n========== GUEST REVIEWS ==========")

    reviews = event_data.get("reviews", [])

    if len(reviews) == 0:
        print("No reviews have been submitted.")
        return

    # Sort reviews from highest rating to lowest
    sorted_reviews = sorted(
        reviews,
        key=lambda review: review["rating"],
        reverse=True
    )

    # Display each review
    for number, review in enumerate(sorted_reviews, start=1):

        print("\n---------- Review", number, "----------")

        print("Guest Name:", review["name"])
        print("Rating:", review["rating"], "/ 5 Stars")
        print("Favorite Part:", review["favorite"])
        print("Least Favorite Part:", review["least_favorite"])
        print("Recommendations:", review["recommendations"])
        print("Organizer Opinion:", review["organizer_opinion"])


# Main function called by main.py
def view_summary_and_reviews(event_data):

    while True:

        print("\n========== SUMMARY AND REVIEWS ==========")
        print("1. Display Event Summary")
        print("2. Submit a Guest Review")
        print("3. Display Guest Reviews")
        print("4. Return to Main Menu")

        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            display_summary(event_data)

        elif choice == "2":
            add_review(event_data)

        elif choice == "3":
            display_reviews(event_data)

        elif choice == "4":
            print("Returning to Main Menu...")
            break

        else:
            print("Invalid choice. Please try again.")
