# x = [2,4,5,45,87,36]
# x1 = []
# for i in x:
#     x1.append(i**2)

# print(x1)

x1 = [1,2,3,4,5]
x2 = [6,7,8,9,10]
# x3 = []
# for i in range (0,len(x1)):
#     x3.append(x1[i] + x2[i])

# for i,j in zip(x1,x2):
#     x3.append(i + j)
# print(x3)


#loops
#comprehension
#>>> newList = [expression forloop condition(optional)]
x3 = [i + j for i,j in zip(x1,x2)]
print(x3)

#lambda expression