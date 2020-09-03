class User:
    def log(self):
        print('logging')


class Teacher(User):
    def log(self):
        print("I'm a teacher")


class Customer(User):
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type
        # print('customer created')

    @property
    def name(self):
        # print('getting name')
        return self._name


    @name.setter
    def name(self, name):
        # print('setting name')
        self._name = name

    @name.deleter
    def name(self):
        # print('deleting name')
        del self._name


    def update_memebership(self, new_membership):
        # print('Calculating costs')
        self.membership_type = new_membership

    def read_customer():
        print('Reading customer from DB')

    def __str__(self):
        return self.name + ' -> ' + self.membership_type

    def print_all_customers(customers):
        print('='*15)
        for el in customers:
            print(el)

    def __eq__(self, other):
        if self.name == other.name and self.membership_type == other.membership_type:
            return True
        return False

    __hash__ = None

    __repr__ = __str__


c = Customer('James', "gold")
print(c)

c2 = Customer('Mike', "bronze")
c3 = Customer('Mike', "bronze")
customers = [c, c2, Teacher()]
customers[0].update_memebership('bronze')
print(customers[0])
# Customer.read_customer()
Customer.print_all_customers(customers)
print(c == c2)
print(c2 == c3)
# data = {customers[0]}
del c3.name
customers[0].log()
customers[2].log()