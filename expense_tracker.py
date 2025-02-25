from datetime import datetime

def user_choice(choice):

	choice = int(input("\nEnter your choice (1-4): "))

	if choice < 1 or choice > 4:

		return false

	else:

		return True 

def get_date(date):
	try:
		datetime.strptime(date, "%d/%m/%Y")
		return True

	except ValueError:
		return false

def get_description(description):

	if description.strip():

		return True

	else:

		return false

def get_amount(amount):

	if amount >= 1:

		eturn True

	else:

		return false



def view_expenses(date_holder, description_holder, amount_holder):

	total_expenses = 0

	for counter in range(len(date_holder)):

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
