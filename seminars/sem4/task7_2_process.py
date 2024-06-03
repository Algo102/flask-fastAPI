from multiprocessing import Process
from random import randint
from time import time

start_time = time()
processes = []

arr = [randint(1, 100) for _ in range(1_000_000)]


def arr_sum(arg):
    res = sum(arg)
    print(f"{res} calculated in {time() - start_time:.2f} seconds")


if __name__ == '__main__':
    print(f"{'-' * 20} Multiprocessing {'-' * 20}")
    for i in range(5):
        p = Process(target=arr_sum, args=(arr,), daemon=True)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()