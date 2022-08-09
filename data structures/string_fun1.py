name = "someTHIng is serious"
print(name)
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())
print(name.swapcase())
print(name.casefold())

word = "python"
print(word.ljust(80))
print(word.rjust(80))
print(word.center(80))

print(word.ljust(80,'-'))
print(word.rjust(80,'&'))
print(word.center(80,'^'))

print('-'*40)
for i in range (1,11):
    r = 3 ** i
    print(3,'x',str(i).rjust(2),'=',r)

