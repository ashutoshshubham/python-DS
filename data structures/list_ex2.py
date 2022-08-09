names = ['Bruce Banner','Captain America','Iron Man']

#comprehension method
initials = [name.split()[0][0]+name.split()[-1][0] for name in names ]
print(initials)

#loop method
initial = []
for name in names:
    parts = name.split()
    initial.append(parts[0][0]+parts[-1][0])
print(initial)