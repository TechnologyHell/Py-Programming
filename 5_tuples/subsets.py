import itertools as it

seta = {10,20,30,40}

s = int(input("Enter the size of subsets : "))
b = set ( it.combinations(seta,s))

print("All possible subsets : ", b)