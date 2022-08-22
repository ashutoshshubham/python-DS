from random import random
from random import randint, choice, choices, shuffle

# value = random()
# print(value) 

nums = []
for i in range(10):
    value = randint(1,1000)
    nums.append(value)
print(nums) 

nums2 = ['5','7','6','3','9','7','6']
sel = choice(nums2)
print(sel)

sel_3_element = choices(nums2, k = 3)
print(" ".join(sel_3_element))

shuffle(nums2)
print(" ".join(nums2))