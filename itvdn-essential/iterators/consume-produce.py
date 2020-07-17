import random, time

def sleep(seconds):
    start = time.time()
    while time.time() - start < seconds:
        yield 


def produce(consumer):
    while True:
        yield from sleep(0.5)
        data = random.randint(1, 100)
        consumer.send(data)


def consume():
    sum_ = 0
    count = 0

    while True:
        data = yield
        print('Got data: ', data)

        sum_ += data
        count += 1

        print('Sum:', sum_)
        print('Average:', sum_/count)
        print()

if __name__ == "__main__":
    consumer = consume()
    next(consumer)

    producer = produce(consumer)
    while True:
        next(producer)