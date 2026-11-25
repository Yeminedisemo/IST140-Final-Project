
# Function to set or update the event budget
def set_budget(event_data):

    print("\n----- Set Event Budget -----")

    # Ask the user to enter a valid budget
    while True:

        budget = input("Enter the event budget: $").strip()

        try:
            budget = float(budget)

            if 0 <= budget < float("inf"):
                event_data["budget"] = budget
                print("\nEvent budget saved successfully!")
                break
            else:
                print("Please enter a valid nonnegative amount.")

        except ValueError:
            print("Invalid input. Please enter a number.")

    # Check if existing expenses exceed the new budget
    if calculate_total(event_data) > event_data["budget"]:
        print("WARNING: You have exceeded your budget!")


# Function to add an expense
def add_expense(event_data):

    print("\n----- Add Expense -----")

    # Check if an event budget has been set
    if "budget" not in event_data:
        print("Please set an event budget first.")
        return

    # Ask the user for the name of the expense
    while True:

        name = input("Enter expense name: ").strip()

        if name != "":
            break
        else:
            print("Expense name cannot be empty.")

    # List of available expense categories
    categories = ["Food", "Venue", "Decorations",
                  "Entertainment", "Transportation", "Other"]

    print("\nSelect an expense category:")

    # Display the available categories
    for number, category in enumerate(categories, start=1):
        print(f"{number}. {category}")

    # Validate the user's category choice
    while True:

        choice = input("Enter your choice (1-6): ").strip()

        if choice.isdecimal() and 1 <= int(choice) <= len(categories):
            category = categories[int(choice) - 1]
            break
        else:
            print("Invalid choice. Please try again.")

    # Ask the user for the cost of the expense
    while True:

        cost = input("Enter the cost of the expense: $").strip()

        try:
            cost = float(cost)

            if 0 <= cost < float("inf"):
                break
            else:
                print("Please enter a valid nonnegative amount.")

        except ValueError:
            print("Invalid input. Please enter a number.")

    # Create a dictionary to store the expense information
    expense = {
        "name": name,
        "category": category,
        "cost": cost
    }

    # Create the expenses list if it does not exist
    if "expenses" not in event_data:
        event_data["expenses"] = []

    # Add the expense to the expenses list
    event_data["expenses"].append(expense)

    print("\nExpense added successfully!")

    # Calculate the total expenses and remaining budget
    total_expenses = calculate_total(event_data)
    remaining_budget = event_data["budget"] - total_expenses

    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Remaining Budget: ${remaining_budget:.2f}")

    # Warn the user if expenses exceed the budget
    if total_expenses > event_data["budget"]:
        print("WARNING: You have exceeded your budget!")


# Function to display all event expenses
def display_expenses(event_data):

    print("\n----- Event Expenses -----")

    expenses = event_data.get("expenses", [])

    # Check if any expenses have been added
    if len(expenses) == 0:
        print("No expenses have been added.")
        return

    # Display each expense and its information
    for number, expense in enumerate(expenses, start=1):

        print("\nExpense", number)
        print("Name:", expense["name"])
        print("Category:", expense["category"])
        print(f"Cost: ${expense['cost']:.2f}")

    print(f"\nTotal Expenses: ${calculate_total(event_data):.2f}")


# Function to calculate the total cost of all expenses
def calculate_total(event_data):

    expenses = event_data.get("expenses", [])

    total_expenses = 0

    # Add the cost of each expense to the total
    for expense in expenses:
        total_expenses += expense["cost"]

    return round(total_expenses, 2)


# Function to display a summary of the event finances
def display_financial_summary(event_data):

    print("\n----- Financial Summary -----")

    # Check if the user has set a budget
    if "budget" not in event_data:
        print("No event budget has been set.")
        return

    # Get the budget and calculate the total expenses
    budget = event_data["budget"]
    total_expenses = calculate_total(event_data)

    # Calculate the remaining budget
    remaining_budget = round(budget - total_expenses, 2)

    # Display the financial information
    print(f"Original Budget: ${budget:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Remaining Budget: ${remaining_budget:.2f}")

    # Check whether the user has exceeded their budget
    if remaining_budget < 0:
        print("WARNING: You have exceeded your budget!")
        print(f"Amount Over Budget: ${abs(remaining_budget):.2f}")

    elif remaining_budget == 0:
        print("You have used your entire budget.")

    else:
        print("You are within your budget.")


# Main function called by main.py
def manage_finances(event_data):

    while True:

        print("\n========== EVENT FINANCES ==========")
        print("1. Set or Update Event Budget")
        print("2. Add Expense")
        print("3. Display All Expenses")
        print("4. Display Financial Summary")
        print("5. Return to Main Menu")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            set_budget(event_data)

        elif choice == "2":
            add_expense(event_data)

        elif choice == "3":
            display_expenses(event_data)

        elif choice == "4":
            display_financial_summary(event_data)

        elif choice == "5":
            print("Returning to Main Menu...")
            break

        else:
            print("Invalid choice. Please try again.")
