import pytz
from datetime import datetime


WHITE = '\033[00m'
GREEN = '\033[0;92m'
RED = '\033[1;31m'


# class Person:
#     def __init__(self, name, surname):
#         self._name = name
#         self._surname = surname
#         self.name = f'{self._name} {self._surname}'


# p = Person('Maxim', 'Smith')
# print(p.name)

class Account:
    def __init__(self, name, balance):
        self.name = name
        self._balance = balance
        self._history = []

    @staticmethod
    def _get_current_time():
        return pytz.utc.localize(datetime.now())

    def deposit(self, amount):
        self._balance += amount
        print(f'Deposit operation of ${amount} completed!')
        self.show_balance()
        self._history.append([amount, self._get_current_time()])

    def withdraw(self, amount):
        if self._balance > amount:
            self._balance -= amount
            print(f'Withdraw {amount} completed!')
            self.show_balance()
            self._history.append([-amount, self._get_current_time()])
        else:
            print('Not enough money')
            self.show_balance()

    def show_balance(self):
        print(f'Your actual balance is ${self._balance}')
        print('='*35)

    def show_history(self):
        for amount, date in self._history:
            if amount > 0:
                transaction = 'deposit'
                color = GREEN
            else:
                transaction = 'withdraw'
                color = RED
            print(f'{color}\t{amount} {WHITE} {transaction} at {date.isoformat()}')



a = Account('Peter', 100)
a.show_balance()
a.deposit(50)
a.deposit(250)
a.withdraw(89)
a.withdraw(50)
a.show_history()
