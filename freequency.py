input_string = input("Enter a string: ")
check = input("Enter the substring to search for: ")
words = input_string.split()
frequency = 0
for word in words:
    if check in word:
        frequency += 1
print(frequency)