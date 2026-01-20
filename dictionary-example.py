'''
Create a Python program that uses a dictionary to
store the names and ages of people. Ask the user to enter
a name, and the program should display the age of that person
'''
user_details = {"Ram":25, "Arun":45}
name = input("Enter your name: ")
print("Age:",user_details.get(name,"User Not Found"))