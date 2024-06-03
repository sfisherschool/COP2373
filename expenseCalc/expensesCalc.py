from functools import reduce

def get_expenses():
    expenses = []
    while True:
        # Ask the user for the type of expense
        expense_name = input("Enter the type of expense (or 'done' to finish): ")
        # If the user types 'done', check if the list is empty
        if expense_name.lower() == 'done':
            # If the list is empty return None
            if not expenses:
                print("Quit out of the program without adding any expenses.")
                return None
            # If the list is not empty, break the loop
            break
        # Ask the user for the amount of the expense in a loop until a valid number is entered
        while True:
            try:
                # Convert the user's input to a float
                expense_amount = float(input(f"Enter the amount for {expense_name}: "))
                # If the conversion is successful, break the loop
                break
            except ValueError:
                # Print an error message and ask again
                print("Please enter a number.")
        # Add the expense to the expenses list as a tuple
        expenses.append((expense_name, expense_amount))

    return expenses

def analyze_expenses(expenses):
    # Adds the amount of the current expense to the running total
    total_expense = reduce(lambda total, expense: total + expense[1], expenses, 0)

    # Compares the amount of the current expense with the amount of the current highest expense
    # If the current expense is higher, it becomes the new highest expense
    highest_expense = reduce(lambda highest, expense: highest if highest[1] > expense[1] else expense, expenses)

    # Compares the amount of the current expense with the amount of the current lowest expense
    # If the current expense is lower, it becomes the new lowest expense
    lowest_expense = reduce(lambda lowest, expense: lowest if lowest[1] < expense[1] else expense, expenses)

    return total_expense, highest_expense, lowest_expense

def main():
    # Get the expenses from the user
    expenses = get_expenses()
    # If the user entered at least one expense, analyze the expenses
    if expenses is not None:
        # Analyze the expenses
        total, highest, lowest = analyze_expenses(expenses)
        # Print the results
        print(f"\nTotal expense: ${total:.2f}")
        print(f"Highest expense: {highest[0]} with ${highest[1]:.2f}")
        print(f"Lowest expense: {lowest[0]} with ${lowest[1]:.2f}")

if __name__ == "__main__":
    main()
