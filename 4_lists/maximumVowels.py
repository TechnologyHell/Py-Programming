list = []
vowel = "aeiou"
max = 0
index = -1
count = 0

size = int(input("Enter the size of list : "))

for i in range (size) : 
    list.append(input("enter the elements : "))


for i in list : 
    count = 0
    for j in i :
        if ( j in vowel ):
            count = count + 1
    if ( count > max ) :
        max = count
        index += 1

print("Element with maximum vowels : ",list[index], " with %d vowels" %(count))