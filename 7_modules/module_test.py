import def_module

a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))

ch = int(input("1 for Add\n2 for Subtract\n3 for Multiply\n4 for Divide\nEnter the choice : "))

if ( ch == 1 ) :
    print(def_module.add(a,b))