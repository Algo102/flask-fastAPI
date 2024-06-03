# Загрузка в 5 потоков с использованием потоков (модуля threading)
# Задание №1
# Записать программу, которая считывает список из 10 URL-адресов и
# одновременно загружает данные с каждого адреса.
# После загрузки данных нужно записать их в отдельные файлы.
# Используйте потоки.

from pathlib import Path

import requests
import threading
import time

urls = ['https://www.google.ru/',
        'https://gb.ru/',
        'https://ya.ru/',
        'https://www.python.org/',
        'https://habr.com/ru/all/',
        ]


def download(url):
    response = requests.get(url)
    filename = 'thread_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
    file_path = Path(path_download, filename)
    with open(file_path, "w", encoding='utf-8') as f:
        f.write(response.text)
    print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")


if __name__ == '__main__':
    path_download = Path(Path.cwd(), 'downloads')
    if not path_download.is_dir():
        path_download.mkdir(parents=True, exist_ok=True)

    threads = []
    start_time = time.time()
    for url in urls:
        thread = threading.Thread(target=download, args=[url])
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
