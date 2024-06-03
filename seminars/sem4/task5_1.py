# Задание №5.
# Создать программу, которая будет производить подсчёт количества слов в
# каждом файле в указанной директории и выводить результаты в консоль.
# Используйте процессы.
import os
import multiprocessing
import time

# MY_PATH = 'downloads'
MY_PATH = 'C:\\Users\\Algor\\Desktop\\GB\\Фреймворки Flask и FastAPI\\flask_fastAPI\\seminars\\sem4\\downloads'

def worker(file_):
    with open(file_, 'r', encoding='utf-8') as f:
        file_name = str(file_).split("\\")[-1]
        print(f'  Слов в файле {file_name} : {len(f.read().split())}')


if __name__ == '__main__':

    multiprocess = []
    start = time.time()
    for root, dirs, files in os.walk(MY_PATH):

        for fil in files:
            file_path = os.path.join(root, fil)
            t = multiprocessing.Process(target=worker, args=(file_path,))
            multiprocess.append(t)
            t.start()
    for t in multiprocess:

        t.join()
    print(f'Время работы: {time.time() - start:0.04f} sec')

