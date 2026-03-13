# Python program to illustrate the use of
# Accessor and Mutator methods

# Defining class Car
class Car:

	# Defining method init method with a parameter
	def __init__(self, carname):
		self.__make = carname

	# Defining Mutator Method
	def set_make(self, carname):
		self.__make = carname

	# Defining Accessor Method
	def get_make(self):
		return self.__make
mycar = Car("Tata")
mycar.set_make("Maruthi")
print(mycar.get_make())

