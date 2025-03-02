import linear_search

array = []
size = int(input("Enter the size of array : "))

print("Enter the elements : ")
for i in range (size) :
    element = int(input())
    array.append(element)

x = int(input("Enter the number to search  : "))

index = linear_search.lsearch(array, x)

if index == -1 :
    print("Element not found.")
else:
    print("Element found at position ", index+1)