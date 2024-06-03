import threading
import os
import time

# MY_PATH = 'downloads'
MY_PATH = 'C:\\Users\\Algor\\Desktop\\GB\\Фреймворки Flask и FastAPI\\flask_fastAPI\\seminars\\sem4\\downloads'


def worker(file_):
    with open(file_, 'r', encoding='utf-8') as f:
        file_name = str(file_).split("\\")[-1]
        print(f' Слов в файле {file_name} : {len(f.read().split())}')


def process_files_in_dir(directory):
    threads = []

    for root, dirs, files in os.walk(directory):
        for fil in files:
            file_path = os.path.join(root, fil)
            t = threading.Thread(target=worker, args=(file_path,))
            threads.append(t)
            t.start()

    for t in threads:
        t.join()


if __name__ == '__main__':
    start = time.time()
    process_files_in_dir(MY_PATH)
    print(f'Время работы: {time.time() - start:0.04f} sec')
