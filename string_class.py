'''
Python class that has two methods: get_String and
print_String , get_String accept a string from the
user and print_String prints the string in upper case

'''
class string_class:
    def get_string(self):
        self.text = input("Enter a string: ")
    def print_string(self):
        print(self.text.upper())

demo = string_class()
demo.get_string()
demo.print_string()

