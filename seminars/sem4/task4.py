# Задание №4.
# Создать программу, которая будет производить подсчёт количества слов в
# каждом файле в указанной директории и выводить результаты в консоль.
# Используйте потоки. (НО ЕСЛИ БУДЕТ БОЛЬШОЕ КОЛИЧЕСТВО ФАЙЛОВ ВСЕ ЗАВИСНЕТ)
import os
import threading
from pathlib import Path

file_dir = Path(Path.cwd(), 'downloads')


def count_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        # print(f'Количество слов в файле {file_path} равно: {len(f.read().split())}')
        file_name = str(file_path).split("\\")[-1]
        word_count = len(f.read().split())
        print(f'Количество слов в файле {file_name} равно: {word_count}')


if __name__ == '__main__':
    threads = []
    for file in os.listdir(file_dir):
        if Path(file_dir, file).is_file():
            thread = threading.Thread(target=count_words, args=(Path(file_dir, file),))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()
