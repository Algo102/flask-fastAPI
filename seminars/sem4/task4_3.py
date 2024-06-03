import threading
import os
import time
import logging
from pathlib import Path

# Через os.walk(), чтоб рекурсивно искал файлы во вложенных папках

# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.basicConfig(level=logging.INFO, format='%(message)s')
loger = logging.getLogger(__name__)


def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        # file_name = str(file_path).split("\\")[-1]
        # print(f' Слов в файле {file_name} : {len(f.read().split())}')
        contents = f.read()
        count_word = len(contents.split())
        # print(f'{f.name} содержит {count_word} слов')
        loger.info(f'{f.name} содержит {count_word} слов')


def main():
    dir_path = Path('downloads')
    # dir_path = Path('C:\\Users\\Algor\\Desktop\\GB\\Фреймворки Flask и FastAPI\\flask_fastAPI\\seminars\\sem4\\downloads')
    file_paths = os.walk(dir_path)

    threads = []
    for root, dirs, files in file_paths:
        for file in files:
            t = threading.Thread(target=process_file(os.path.join(root, file)))
            threads.append(t)
            t.start()

    for t in threads:
        t.join()

    loger.info('Finish')
    # print('Finish')


if __name__ == '__main__':
    start = time.time()
    main()
    print(f'{time.time() - start:0.3f} sec')
