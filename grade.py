passes = 0

failures = 0

for student in range(10):

	result = int(input("Enter result (1 is pass, 2 is fail): "))

	if result == 1:

		passes = passes + 1

	else:
		
		failures = failures + 1

print("passed ", passes)

print("failed ", failures)

if passes > 6:

	print("Bonus to instructor")