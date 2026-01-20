'''
Define a function named summation.
This function expects two numbers, named low and high,
as arguments. The function computes and returns the sum of
the numbers between low and high, inclusive.
'''
def summation(low, high):
    sum=0
    for i in range(low, high+1):
        sum = sum+ i
    return sum
print(summation(3, 9))