'''Problem Statement: Create a Python class Vehicle with attributes registration_number, type, and owner. Implement a method update_owner to change the vehicle's owner. Then, create a few instances of Vehicle and demonstrate changing the owner.'''
from helper import d

class Vehicle:
        def __init__(self, reg_num, type, owner):
            '''This method initializes the attributes of the Vehicle class'''
            self.registration_number = reg_num
            self.type = type
            self.owner = owner

        def update_owner(self, new_owner):
            '''This method updates the owner of the vehicle'''
            self.owner = new_owner
            print(f"{self.owner} is now the new owner of the {self.type}")

        def get_info(self):
            '''This method prints the type of vehicle and its owner.'''
            print(f"The owner of the {self.type} is {self.owner}")

# Create instances of the Vehicle class and demonstrate changing the owner

Ferrari = Vehicle('REG2345434', 'Sports Car', 'Aurthor Morgan')
Tahoe = Vehicle('REG2364478', 'SUV', 'Michael Smith')
Bently = Vehicle('REG2568874', 'Luxury Car', 'Mary Jane')
Accord = Vehicle('REG94336', 'Sedan', 'Justin Jacobs')
Audi = Vehicle('REG987678', 'Luxury Coupe', 'John Doe')

Ferrari.update_owner('Michael Jackson')
Tahoe.update_owner('George Clooney')
Bently.update_owner('Prince')
Accord.update_owner('Elvis Presley')
Audi.update_owner('Marilyn Monroe')

d()
# For redundancy, we are checking to make sure the owners of the vehicles did, in fact, change.

Ferrari.get_info()
Tahoe.get_info()
Bently.get_info()
Accord.get_info()
Audi.get_info()

d()


