"""
import copy
bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)
bus1.drop('Bill')
bus2.passengers
['Alice', 'Claire', 'David']
bus3.passengers
['Alice', 'Bill', 'Claire', 'David']

"""

# tag::BUS_CLASS[]
class Bus:

    def __init__(self, passengers: list[str] | None =None):
        print(f'id(passengers): {id(passengers)}')
        if passengers is None:
            self.passengers: list[str] = []
        else:
            self.passengers = list(passengers)
            print(f'id(self.passengers): {id(self.passengers)}')

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)
# end::BUS_CLASS[]


import copy
bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)
print(id(bus1), id(bus2), id(bus3))

bus1.drop('Bill')
print(bus2.passengers)
         
print(id(bus1.passengers), id(bus2.passengers), id(bus3.passengers))
print(bus3.passengers)


