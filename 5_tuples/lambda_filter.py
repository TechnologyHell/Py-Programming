t1 = ( (1,2,3) , (1,2,-3), (-1,-2,-3), (1,5,9) )

new = tuple ( filter ( lambda x : all ( i>0 for i in x), t1))

print("Positively filtered values : ", new)