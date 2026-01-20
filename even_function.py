'''
Define a function named even. This function expects a
number as an argument and returns True if the number
is divisible by 2, or it returns False otherwise.
(Hint: A number is evenly divisible by 2 if the remainder is 0.)
'''
def even(n):
    if n % 2 == 0:
        return True
    else:
        return False
number = int(input("Enter a number: "))
if(even(number)):
    print("Even")
else:
    print("Not Even")