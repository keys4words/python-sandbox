import random
from decimal import Decimal
import datetime

print(random.random())
print(random.randint(1, 100))
print(random.choice(['first', 'second', 'third']))
print(random.choice(['first', 'second', 'third']))
print(random.sample(range(100), 16))
print(Decimal('0.1')+Decimal('0.3')**Decimal('0.5'))
now = datetime.datetime.now()
print(now)
print(datetime.datetime.now()-now)
print(datetime.timedelta(0, 131, 345345))