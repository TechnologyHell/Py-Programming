str = input("Enter a string : ")

l = str.split()

lower = [x for x in l if x.islower()]
upper = [y for y in l if y.isupper()]

print("Lowercase : ", lower)
print("Uppercase : ", upper)