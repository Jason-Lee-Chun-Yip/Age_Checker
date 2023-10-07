driving = input('Have you drove before? Yes or No: ')
if driving != 'Yes' and driving != 'No':
	print('Just answer Yes or No !!! ')
	raise SystemExit

age = int(input('What is your age? : '))

if driving == 'Yes':
	if age >= 18:
		print('Pass the test !!! ')
	else:
		print('Is illegal !!! ')
elif driving == 'No':
	if age >= 18:
		print('You should get yourself a driving license! ')
	else:
		print('You are eligible for driving exam in the next few years !!!')
