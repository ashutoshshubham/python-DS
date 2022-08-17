# my_dict = {'name' : "Ashu","age" : 24}
# print(my_dict)

# print(my_dict['name'])

# print(my_dict.get('age'))  #prefered method to get value of given key

# print(my_dict['address'])

# print(my_dict.get('name'))

# print(my_dict.get('age'))

# print(my_dict.get('address'))



# #update Value
# my_dict['age'] = 25

# #add items
# my_dict['address'] = 'Lucknow'
# print(my_dict)


sq = {1:1,2:4,3:9,4:16,5:25}
# print(sq.pop(4))

# print(sq.popitem())  #remove arbitrary item

# sq.clear()

# del sq 

for i in sq:
    print(i)

for i in sq:
    print(sq[i])

for k,v in sq.items():
    print(k,v)