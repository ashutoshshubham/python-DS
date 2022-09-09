x = [1,2,3,4,2,3,5,4,3]

# x1 = map(lambda i : i ** 2, x)
# print(list(x1))

         #OR

x1 = list(map(lambda i : i ** 2, x))
print(x1)

x2 = tuple(map(lambda i : i ** 3, x))
print(x2)




y = ['apple', 'banana', 'cherry']
z = ['pie', 'shake', 'jam']

words = set(map(lambda a,b : a+'-'+b, y,z))
print(words)


#single line input with multiple values

numbers = list(map(int,input('Enter 10 numbers : ').split()))
print(numbers)
