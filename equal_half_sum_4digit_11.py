"""
Generate and display all four‑digit numbers such that:
The sum of the first two digits equals the sum of the last two digits,
and the number is divisible by 11.
"""
for num in range(1000,10000):
    fourth_digit = num // 1000  # thousands
    third_digit = (num // 100) % 10  # hundreds
    second_digit = (num // 10) % 10  # tens
    first_digit = num % 10  # units
    if(num %11 ==0) and (fourth_digit+third_digit == first_digit+second_digit):
        print(num, end=" ")