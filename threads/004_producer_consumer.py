import threading, time

def producer():
    time.sleep(10)
    print('Product produced!')
    product.set()
    product.clear()


def consumer():
    print('Wait for product!')
    product.wait()
    print('Product consumed!')


product = threading.Event()
task1 = threading.Thread(target=producer)
task2 = threading.Thread(target=consumer)

task1.start()
task2.start()
task1.join()
task2.join()
