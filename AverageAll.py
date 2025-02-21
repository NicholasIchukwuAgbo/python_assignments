total = 0
largest = integer.MIN_VALUE
smallest = integer.MAX_VALUE

for count in range (1,  11):
	number = float(input(f"Enter score {count}: "))

total += number

             
print("Sum:", total)
print("Largest is: ", largest)
print("Smallest is: ", smallest)
