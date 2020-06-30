class NumberGenerator:
    def __init__(self):
        self.current = 0
    def get_next(self):
        self.current += 1
        return self.current

class House:
    def __init__(self, floors_qty, apartments_on_floor):
        number_generator = NumberGenerator()
        self.floors = []
        for i in range(floors_qty):
            self.floors.append(Floor(i+1, apartments_on_floor, number_generator))
    def settle(self, owner):
        for floor in self.floors:
            apartment = floor.get_free_apartment()
            if apartment is not None:
                apartment.add_owner(owner)
                break
    def __str__(self):
        res = 'House:\n'
        for floor in self.floors:
            res += (str(floor) + '\n')
        return res


class Floor:
    DEFAULT_APARTMENTS_ON_FLOOR = 4
    def __init__(self, number, apartments_on_floor, number_generator):
        self.number = number
        self.apartments = []
        for i in range(apartments_on_floor):
            self.apartments.append(Apartment(number_generator.get_next(), Floor.DEFAULT_APARTMENTS_ON_FLOOR))

    def get_free_apartment(self):
        for apartment in self.apartments:
            if apartment.is_free():
                # print('apartment is free')
                return apartment
        raise ValueError('There is no free apartments')
    def __str__(self):
        res =  'Floor #' + str(self.number) + '\n'
        res += ('-'*30 + '\n')
        for apartment in self.apartments:
            res += (str(apartment) + '\n')
        return res

class Owner:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f'{self.name}'

class Apartment:
    def __init__(self, number, owners_qty):
        self.number = number
        self.owners_qty = owners_qty
        self.owners = []
        for i in range(owners_qty):
            self.owners.append("empty")
    def get_free_room_index(self):
        for i in range(self.owners_qty):
            if self.owners[i] == "empty":
                return i
        raise ValueError('No free rooms at the floor')
    def add_owner(self, owner):
        self.owners[self.get_free_room_index()] = owner
    def is_free(self):
        return self.owners[self.owners_qty - 1] == "empty"
    def __str__(self):
        res = 'Apartment #' + str(self.number) + '\n'
        for i in range(len(self.owners)):
            if self.owners[i] != "empty":
                res += '*' * 20 + '\n'
                res += 'Owner: ' + str(self.owners[i]) + '\n'
        return res


house = House(2, 4)
owner1 = Owner("Steven Spielberg")
owner2 = Owner("James Cameron")
house.settle(owner1)
house.settle(owner2)
print(house)