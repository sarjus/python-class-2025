'''
Write a Python program that performs the following tasks:
Accept a positive integer from the user.
Count how many even digits and how many odd digits are present in the number.
After counting:
Print “Balanced” if the number of even and odd digits are equal.
Print “More even digits” if the count of even digits is higher.
Print “More odd digits” if the count of odd digits is higher.

'''
input_number = int(input("Enter a positive integer: "))
even_digits = 0
odd_digits = 0
while input_number > 0:
    digit = input_number % 10
    if digit % 2 == 0:
        even_digits += 1
    else:
        odd_digits += 1
    input_number = input_number // 10
print("Even digits:" ,even_digits)
print("Odd digits:",odd_digits)
if(even_digits > odd_digits):
    print("More even digits")
elif(odd_digits > even_digits):
    print("More odd digits")
else:
    print("Balanced")