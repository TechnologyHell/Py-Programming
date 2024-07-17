list = []

size = int(input("Enter the size of list : "))

for i in range (size) : 
    list.append(input("Enter values into the list : "))

value = int(input("Enter the value for incrementing number : "))

for i in range ( size ) :
    if ( list[i] . isdigit() ):
        list[i] = str ( int ( list[i] ) + value )

print("Incremented List : ")
print(list)