dict = {'A' : 10 , 'B' : 11 , 'C' : 3 , 'D' : 2}

L1 = list ( sorted ( dict.values() ) )
L2 = list ( sorted ( dict.values(), reverse=True ) )

print("Ascending Order : ", L1)
print("Descending Order : ", L2)