#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = 20
gusses = 9
print("You have 9 gusses")
for i in range (1,10):
    num = int(input("Enter the number "))
    if (num == 20):
        print(f"Bingo! You found my number in {i} gusses")
        break
    elif (num > 10 and num <= 15) or (num >= 25 and num < 30):
        print("Little close\nNumber of gusses remaining ",gusses-i)
    elif (num > 15 and num < 20) or (num > 20 and num < 25):
        print("Too close\nNumber of gusses remaining ",gusses-i)
    else:
        print("Too Far\nNumber of gusses remaining ",gusses-i)
    
if (i == 9 and num != 20):
    print("Better Luck Next Time!")
input()


# In[ ]:





# In[ ]:




