n = int(input("Enter a number: "))
b =0
i=1
while n>0:
    r = n % 2
    b= r*i +b
    i =i * 10
    n = n//2
print(b)