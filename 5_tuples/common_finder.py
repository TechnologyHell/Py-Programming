def common_finder ( x , y , z ):
    l1 = set(x)
    l2 = set(y)
    l3 = set(z)

    result = list ( l1 & l2 & l3 )

    return (result)


print("Enter elements into list 1 : ")
x = map ( int, input() . split(' '))

print("Enter elements into list 2 : ")
y = map ( int, input() . split(' '))

print("Enter elements into list 3 : ")
z = map ( int, input(). split(' '))

print("Common elements between the 3 lists are : ")

res = [] 
res = common_finder(x,y,z)
print(res)