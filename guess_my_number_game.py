import random

print("Welcome to my guessing game")

start = int(input("Enter starting point: "))

end = int(input("Enter ending point: "))

chances = ['life', 'life', 'life', 'life', 'life']

win = "Congratulations:), you've guessed the correct number, 5,000 WON"

lose = "oga, oga, oga... You don lose"

guessing = 0

my_number = random.randint(start, end)

#print(my_number)

while 'life' in chances:

	try:
		guessing = int(input(f"Guess a number between({start} - {end}): "))

		if guessing < start or guessing > end:

			print(f"choose btw ({start} - {end})")

		else:

			if guessing > my_number:

				chances.remove('life')

				chances.append('otilo')

				print(f"Your guess is too high {chances}")

			elif guessing < my_number:

				chances.remove('life')

				chances.append('otilo')

				print(f"Your guess is too low {chances}")

	except ValueError:

		print("invalid input, try again")

	if guessing == my_number:

		print(win)

		break

if 'life' not in chances:

	print(lose)

print(f'The actual value is: {my_number}')
