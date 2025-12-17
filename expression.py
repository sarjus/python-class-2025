# (a+b)2 = a2+2ab+b2
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
lhs = (a+b)*(a+b)
rhs = a**2+(2*a*b)+b**2
print(lhs == rhs)
