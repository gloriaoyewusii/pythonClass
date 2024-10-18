x = 2 
y = 3

print('x =', x)
print('Value of', x, '+', x, 'is', (x + x))
print('x =')
print((x + y), 'x =', (y + x))

rating = input('Enter an integer rating between 1 and 10: ')
print("rating is", rating)

grade = int(input('Enter a grade: '))
if (grade >= 90):
	print('Congratulations! Your grade of', grade, 'earns you an A in this course')