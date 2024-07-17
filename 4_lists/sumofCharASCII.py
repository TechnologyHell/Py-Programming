list = []
new = []

size = int(input("Enter the size of List : "))

for i in range( size ) :
    list.append(input("Enter the elements : "))

sum = 0

for i in list : 
    for j in i : 
        sum = sum + ord(j)
    new.append(sum)
    sum = 0

print("Sum of ASCII values of the items : ")
print(new)