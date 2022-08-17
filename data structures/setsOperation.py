#Union
A = {1,2,3,4,5}
B = {4,5,6,7,8}
print(A | B)

print(A.union(B))

print(B.union(A))

#intersection
print(A & B)

print(A.intersection(B))

#difference
print(A - B)

print(A.difference(B))

print(B.difference(A))

#symmetric Difference
print(A ^ B)

print(A.symmetric_difference(B))

#issubset isdisjoint
x = {2,3,4,5}
y = {2,3,4,5,6,7,8}

print(x.issubset(y))

z = {1,9,10}

print(x.issubset(z))

a = {11,12,13}

print(a.isdisjoint(y))

#remove duplicate

a1 = [2,2,5,4,7,7]
print(list(set(a1)))