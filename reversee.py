def isReverse(reverse: int) -> int:

	backward = 0

	original = reverse

	while reverse > 0:

		number = reverse % 10
	
		backward = backward * 10 + number

		reverse //= 10

	return backward

nums = 2345

print(isReverse(nums))
