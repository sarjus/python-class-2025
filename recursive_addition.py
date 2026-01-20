'''
Add two integer number using recursive addition
'''
def recursive_addition(num1, num2):
    if num2==0:
        return num1
    else:
        return num1+recursive_addition(num1+1,num2-1)

result = recursive_addition(12,13)
print(result)