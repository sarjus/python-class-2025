'''
Create a function min_max() that takes n numbers as list
argument and return the smallest and largest numbers.

'''

def min_max(numbers):
    result = []
    numbers.sort()
    result.append(numbers[0])#smallest number
    result.append(numbers[-1]) #largest number
    return result
numbers = [43,12,56,20,5,8,10]
result=min_max(numbers)
print(f"smallest number is {result[0]}")
print(f"largest number is {result[-1]}")
