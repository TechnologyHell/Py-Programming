import bubble_sort

array = []
size = int(input("Enter the size of array : "))

print("Enter the elements : ")
for i in range (size) :
    element = int(input())
    array.append(element)

print("Default Array : ")
print(array)

sorted_array = bubble_sort.bsort (array, size)
print("After sorting : ")
print(array)