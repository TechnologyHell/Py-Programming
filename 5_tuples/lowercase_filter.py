a = map (tuple, input ("Enter the elements : ").split(' '))

lower = []

for x in a:
    for y in x :
        if y.islower() :
            lower.append(y)

print("Lower case filtered characters are : ")
print(lower)