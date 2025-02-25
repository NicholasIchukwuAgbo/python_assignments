from datetime import datetime

def user_choice():

	while True:

		try:
			choice = int(input("\nEnter your choice (1-4): "))

			if choice < 1 or choice > 4:

				print("Invalid choice, choose between (1-4)")

			else:

				return choice 

		except ValueError:

			print("Invalid input. Please enter a number.")

def get_date():

	while True:

		date = input("\nEnter the date (DD/MM/YYYY): ")

		try:

			datetime.strptime(date, "%d/%m/%Y")

			return date

		except ValueError:

			print("Invalid date format")

def get_description():

	while True:

		description = input("Enter the description: ")

		if description.strip():

			return description

		else:

			print("Description cannot be empty")

def get_amount():

	while True:

		try:

			amount = float(input("Enter the amount: "))

			if amount >= 1:

				return amount

			else:

				print("Amount must be greater than or equal to 1")

		except ValueError:

			print("Invalid input, must be a number")


def add_expense(date_holder, description_holder, amount_holder):

	date_place_holder = get_date()

	date_holder.append(date_place_holder)

	description_place_holder = get_description()

	description_holder.append(description_place_holder)

	amount_place_holder = get_amount()

	amount_holder.append(amount_place_holder)

def view_expenses(date_holder, description_holder, amount_holder):

	print("\n:::::Expenses:::::")

	if not date_holder:
		print("Nothing to display")

	total_expenses = 0

	for counter in range(len(date_holder)):

		print(f"{counter + 1}. Date: {date_holder[counter]}, Description: {description_holder[counter]}, Amount: {amount_holder[counter]}")

		total_expenses += amount_holder[counter]

	return total_expenses

def calculate_total_expenses(total_expenses):

	return total_expenses

def main():

	print("=========================================")
	print(" Welcome To Semicolon Tracker App")
	print("=========================================\n")

	date_holder = []

	description_holder = []

	amount_holder = []

	total_expenses = 0

	while True:

		print("\n 1. Add on expense. \n 2. View all expenses. \n 3. Calculate total expenses. \n 4. Exit.")

		choice_place_holder = user_choice()

		if choice_place_holder == 1:

			add_expense(date_holder, description_holder, amount_holder)
			print("\nExpense Added!")

		elif choice_place_holder == 2:

			view_expenses(date_holder, description_holder, amount_holder)

		elif choice_place_holder == 3:

			calculate_total_expenses(total_expenses)

			print(f"\nTotal Expenses: {total_expenses}")

		elif choice_place_holder == 4:

			print("\nExiting the app. Goodbye!")

			break



if __name__ == "__main__":
	main()
