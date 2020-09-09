import threading

def producer():
    print('set locking')
    with lock:
        print('done')
        with lock:
            print("it's great")
    print('locking release')


lock = threading.RLock()

task1 = threading.Thread(target=producer)
task2 = threading.Thread(target=producer)

task1.start()
task2.start()
task1.join()
task2.join()