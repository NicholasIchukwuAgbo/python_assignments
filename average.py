total = 0

grade_counter = 0

grades = [98, 34, 75, 24, 98, 45, 76, 12, 39, 35]

for grade in grades:

	total += grade

	grade_counter += 1

average = total / grade_counter

print(f'Average is: {average}') 