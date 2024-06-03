# Задание №7.
# Напишите программу на Python, которая будет находить сумму элементов массива
# из 1000000 целых чисел.
# Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, …].
# Массив должен быть заполнен случайными целыми числами от 1 до 100.
# При решении задачи нужно использовать многопоточность, многопроцессорность и
# асинхронность.
# В каждом решении нужно вывести время выполнения вычислений.

import os
import threading
import multiprocessing
import asyncio
from pathlib import Path
from random import randint
import time

count = 0

# main_lst = [randint(1, 101) for _ in range(1_000_000)]
main_lst = [i for i in range(1_000_000)]


def increment(lst_num):
    global count
    for num in lst_num:
        count += num
    print(count)


if __name__ == '__main__':
    start_time = time.time()
    threads = []
    lst_num = [main_lst[i:i+100_000] for i in range(10)]
    for i in range(10):
        t = threading.Thread(target=increment, args=(lst_num[i],))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f'All threads finished in {time.time()-start_time:0.03f} sec')
