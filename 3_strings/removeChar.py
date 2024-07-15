def remove( str, n ):
    a = str[ : n-1]
    a = a + str[ n : ]
    return a


str = input("Enter a string : ")
pos = int(input("Enter the position to remove : "))
print(remove(str, pos))