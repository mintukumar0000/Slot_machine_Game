from expense import Expense
import calendar
import datetime

def main():
    budget = 2000
    file_path = "/Users/mintukumar/Desktop/Cursor_AI/Projects/Expense tracker/expenses.csv"

    # Get and save expense
    expense = get_user_expense()
    save_expense_to_file(expense, file_path)

    # Summarize expenses
    summarize_expenses(file_path, budget)

def get_user_expense():
    name = input("Enter the name: ")
    amount = float(input("Enter the amount: "))
    categories = ["Food", "Home", "Work", "Fun", "Misc", "Other"]

    while True:
        print("Select a category:")
        for i, category in enumerate(categories):
            print(f"{i + 1}. {category}")

        selected_index = int(input("Select a category number: ")) - 1

        if 0 <= selected_index < len(categories):
            category = categories[selected_index]
            return Expense(name=name, amount=amount, category=category)
        else:
            print("Invalid category number. Please try again.")

def save_expense_to_file(expense, file_path):
    with open(file_path, "a") as f:
        f.write(f"{expense.name},{expense.category},{expense.amount}\n")

def summarize_expenses(file_path, budget):
    expenses = []
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()

            for line in lines:
                name, category, amount = line.strip().split(",")
                expenses.append(Expense(name, category, float(amount)))

    except FileNotFoundError:
        print(f"Error: File {file_path} not found. Please ensure the file exists.")
        return

    # Calculate total spent and remaining budget
    total_spent = sum(exp.amount for exp in expenses)
    remaining_budget = budget - total_spent

    print("\n--- Expense Summary ---")
    print(f"Total spent: ${total_spent:.2f}")
    print(f"Remaining budget: ${remaining_budget:.2f}")

    # Group expenses by category
    category_totals = {}
    for expense in expenses:
        if expense.category in category_totals:
            category_totals[expense.category] += expense.amount
        else:
            category_totals[expense.category] = expense.amount

    print("\nExpenses by Category:")
    for category, total in category_totals.items():
        print(f"  {category}: ${total:.2f}")

def green(text):
    return f"\033[92m{text}\033[0m"
if __name__ == "__main__":
    main()
