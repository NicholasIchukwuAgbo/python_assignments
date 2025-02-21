def searching(number:int, search:int) -> int:
	count = 0
	j = str(number)
	for k in j:
		if search == int(j):
			count += 1
	return count;

number = input("Enter numbers: ")

target = input("Enter target: ")

print(searching(number, target))