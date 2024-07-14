def hcf(x,y):
    while(y!=0):
        r = x%y
        x = y
        y = r
    return x

def lcm(x,y):
    lcm = (x*y) / hcf(x,y)
    return lcm

x,y = map(int,input("Enter 2 numbers : ").split(' '))
print("HCF : ", hcf(x,y))
print("LCM : ", lcm(x,y))