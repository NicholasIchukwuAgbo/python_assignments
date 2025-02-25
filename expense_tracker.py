from datetime import datetime

def get_date(date):

	try:

		datetime.strptime(date, "%d/%m/%Y")

		return True

	except ValueError:

		return False

def get_description(description):

	if description.strip():

		return True

	else:

		return False

def get_amount(amount):

	if amount >= 1:

		return True

	else:

		return False



def view_expenses(date_holder, description_holder, amount_holder):

	total_expenses = 0

	for counter in range(len(date_holder)):

		total_expenses += amount_holder[counter]

	return total_expenses


def calculate_total_expenses(amount_holder):

	total = 0;

	for counter in range(len(amount_holder)):

		total += amount_holder[counter]

	return total  


def main():

	print("=========================================")
	print(" Welcome To Semicolon Tracker App")
	print("=========================================\n")

	date_holder = []

	description_holder = []

	amount_holder = []

	total_expenses = 0

	choice = 0
	
	count = 0

	while True:

		print("\n 1. Add on expense. \n 2. View all expenses. \n 3. Calculate total expenses. \n 4. Exit.")

		try:

			choice = int(input("\nEnter your choice (1-4): "))
	
			if choice < 1 or  choice > 4:

				print("invalid, enter number between 1-4")
		
		except ValueError:

			print("invalid, enter numer")


		if choice == 1:

			count += 1

			while True:

				date = input("\nEnter the date (DD/MM/YYYY): ")

				if get_date(date):

					date_holder.append(date)

					break
				else:
					print("invalid date, date format (DD/MM/YYYY)") 

			while True:

				description = input("Enter the description: ")

				if get_description(description):

					description_holder.append(description)

					break

				else:
					print("Description cannot be empty")


			while True:

				try:

					amount = float(input("Enter the amount: "))

					if get_amount(amount):

						amount_holder.append(amount)

						break

					else:

						print("Amount must be greater than or equal to 1")

				except ValueError:

					print("Invalid input, must be a number")

			print("Expense added!")


		elif choice == 2:

			print("\n::::Expenses::::\n")

			if count == 0:

				print("No expense record yet..")
			else:
				for num in range(len(date_holder)):

					print(f"{num + 1}. Date: {date_holder[num]}, Description: {description_holder[num]}, Amount: {amount_holder[num]}")

		elif choice == 3:

			print(f"\n Total Expenses: {calculate_total_expenses(amount_holder)}")

		elif choice == 4:

			print("\n Exiting the app. Goodbye!")

			break


if __name__ == "__main__":
	main()
