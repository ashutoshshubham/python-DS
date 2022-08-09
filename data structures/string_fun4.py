name = input("what is your name? ")

print(name)
print(f"length: {len(name)}")

cl_name = name.strip() #remove leading and trailing whitespace or characters
print(cl_name)
print(f"length: {len(cl_name)}")

secret_msg = '000000000GOLA000000000'
print(secret_msg.strip('0'))
print(secret_msg.lstrip('0'))
print(secret_msg.rstrip('0'))

crap_msg = ''' 

          Exuse me brother, brother idher!

'''
clean_msg = crap_msg.strip()
print(crap_msg)
print(clean_msg)
print(f'{len(crap_msg)} --> {len(clean_msg)}')