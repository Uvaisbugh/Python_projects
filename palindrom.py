def check_palindrom(string):
	left = 0
	right = len(string) -1

	while left < right :
		if string[left] != string[right]:
			return False
		left += 1
		right -= 1
	return True

result=check_palindrom('madam')
print(result)
