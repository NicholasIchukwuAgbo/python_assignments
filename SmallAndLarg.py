num1 = int(input("Enter first integer: "))

num2 = int(input("Enter second integer: "))

num3 = int(input("Enter third integer: "))

sum = num1 + num2 + num2

print("The sum is: ", sum)

average = sum/3

print("The Average is: ", average)

if (num1 > num2 and num1 > num3):

	print("First integer is the largest: ", num1) 

if (num2 > num1 and num2 > num3):

	print("Second integer is the largest: ", num2)

if (num3 > num1 and num3 > num2):

	print("Third is the largest: ", num3)

if (num1 < num2 and num1 < num3):

	print("First integer is the smallest: ", num1)

if (num2 < num1 and num2 < num3):

	print("Second integer is the smallest: ", num2)

if (num3 < num1 and num3 < num2):

	print("Third integer is the smallest:    ", num3)	
	

