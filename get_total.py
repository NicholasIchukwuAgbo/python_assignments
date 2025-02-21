def get_total(number):

	total = 0
	
	for num in number:

		total += int(num)
	return total

userInput = input("Enter numbers: ")

print(get_total(userInput))