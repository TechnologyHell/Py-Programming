import random 

l = []

size = int(input("Enter the size of list : "))

for i in range (size) : 
    l.append ( random.randint(1,100))

print("List of random numbers : ")
print(l)

sorted = l
sorted.sort()

print("Sorted list : ")
print(sorted)