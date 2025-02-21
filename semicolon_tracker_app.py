from datetime import datetime

print("=========================================")
print("    Welcome To Semicolon Tracker App")
print("=========================================")

date_holder = []
description_holder = []
amount_holder = []
total_expenses = 0
choice = 0

while True:

	print("\n1. Add on expense")
	print("2. View all expenses")
	print("3. Calculate total expenses")
	print("4. Exit")
	
	while True:
		try:
			choice = int(input("\nEnter your choice (1-4): "))
			if choice < 1 or choice > 4:
				print("Invalid choice😡, choose between(1 - 4)")
		except ValueError:
			print("Invalid input😠. Please enter a number.")


	if choice == 1:
		while True:
			try:
				date = input("\nEnter the date (DD/MM/YYYY): ")
				datetime.strptime(date, "%d/%m/%Y")
				date_holder.append(date)
				break
			except ValueError:
				print("Invalid date format")


		while True:
			description = input("Enter the description: ")
			if description.strip():
				description_holder.append(description)
				break	
			else:
				print("Description cannot be empty😒")

		while True:
			try:
				amount = float(input("Enter the amount: "))
				if amount >= 1:
					amount_holder.append(amount)
					break
			except ValueError:
				print("Invalid input😠, must be a number")
	
		print("\nExpense Added!")

	
	elif choice == 2:
		print("\n:::::Expenses:::::")
		
		for counter in range(len(date_holder)):
			print(f"{counter + 1}. Date: {date_holder[counter]}, Description: {description_holder[counter]}, Amount: {amount_holder[counter]}")
			total_expenses += amount_holder[counter]
	
	elif choice == 3:
		print(f"\nTotal Expenses: {total_expenses}")

	elif choice == 4:
		print("\nExisting the app. Goodbye!🙋‍♂️")

		break
	
