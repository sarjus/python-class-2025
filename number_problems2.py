'''
Write a Python program to generate and display all four-digit numbers that satisfy the following conditions:
The sum of the first two digits is equal to the sum of the last two digits.
The number is divisible by 11.
Your program should check every four-digit number and print only those that meet both conditions.
'''
for i in range(1000,10000):
    d1 = i//1000
    d2 = (i//100)%10
    d3 = (i//10)%10
    d4 = i%10
    if (d1+d2)== (d3+d4) and i%11==0:
        print(i)