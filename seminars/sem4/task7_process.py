# # Задание №7.
# # Напишите программу на Python, которая будет находить сумму элементов массива
# # из 1000000 целых чисел.
# # Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, …].
# # Массив должен быть заполнен случайными целыми числами от 1 до 100.
# # При решении задачи нужно использовать многопоточность, многопроцессорность и
# # асинхронность.
# # В каждом решении нужно вывести время выполнения вычислений.

import multiprocessing
# from random import randint
import time

# count = multiprocessing.Value('l', 0)
#
# # main_lst = [randint(1, 101) for _ in range(1_000)]
# main_lst = [i for i in range(1_000_000)]
#
#
# def increment(cnt, lst_num):
#     for num in lst_num:
#         with cnt.get_lock():
#             cnt.value += num
#     print(cnt.value)
#
#
# if __name__ == '__main__':
#     start_time = time.time()
#     processes = []
#     lsts_nums = [main_lst[i:i + 100000] for i in range(10)]
#     for lst in range(10):
#         p = multiprocessing.Process(target=increment, args=(count, lsts_nums[lst],))
#         processes.append(p)
#         p.start()
#
#     for p in processes:
#         p.join()
#
#     print(f'All processes finished in {time.time()-start_time:0.03f} sec')


# Другое решение, т.к. код с еминара у меня работал не верно
count = multiprocessing.Value('q', 0)
main_lst = [i for i in range(1_000_000)]


def increment(cnt, lst_num):
    local_sum = sum(lst_num)
    with cnt.get_lock():
        cnt.value += local_sum
    print(cnt.value)


if __name__ == '__main__':
    start_time = time.time()
    processes = []
    lsts_nums = [main_lst[i:i + 100000] for i in range(10)]
    for lst in range(10):
        p = multiprocessing.Process(target=increment, args=(count, lsts_nums[lst],))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print(f'All processes finished in {time.time()-start_time:0.03f} sec')
    # print(f'Total sum: {count.value}')


# # Переделала ИИ на основе ассинхронного кода

# main_lst = [i for i in range(1_000_000)]
#
#
# def increment(lst_num):
#     local_count = sum(lst_num)
#     return local_count
#
#
# def main():
#     pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
#     chunk_size = len(main_lst) // multiprocessing.cpu_count()
#     lsts_nums = [main_lst[i:i + chunk_size] for i in range(0, len(main_lst), chunk_size)]
#     result = sum(pool.map(increment, lsts_nums))
#     print(f'Sum of array elements: {result}')
#
#
# if __name__ == '__main__':
#     start_time = time.time()
#     main()
#     print(f'All processes finished in {time.time()-start_time:0.03f} sec')


# # Переделала ИИ на основе многопоточного кода

# main_lst = [i for i in range(1_000_000)]
#
#
# def increment(lst_num, result):
#     local_sum = sum(lst_num)
#     result.put(local_sum)
#
#
# if __name__ == '__main__':
#     start_time = time.time()
#     processes = []
#     result_queue = multiprocessing.Queue()
#     lst_num = [main_lst[i:i+100_000] for i in range(10)]
#     for i in range(10):
#         p = multiprocessing.Process(target=increment, args=(lst_num[i], result_queue))
#         processes.append(p)
#         p.start()
#
#     for p in processes:
#         p.join()
#
#     total_sum = 0
#     while not result_queue.empty():
#         total_sum += result_queue.get()
#
#     print(f'All processes finished in {time.time()-start_time:0.03f} sec')
#     print(f'Total sum: {total_sum}')
