x, y = map(int, input("Enter the range : ").split(' '))

print("Prime numbers between the following range are : ")

for i in range( 2, y ) :
    flag = 1
    for j in range( 2, i) :
        if ( i % j == 0) :
            flag = 0
            break
    if( flag == 1 ) : 
        print(i)