def find_even(number:str) -> int:

	total = 0

	for char in number:
	
		if char.isnumeric():
  
			temp = int(char)
	
			if temp % 2 == 0:
	
				total += temp
	return total


userInput = input("Enter any number and letters: ")

print(find_even(userInput))



	