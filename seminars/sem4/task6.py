# Задание №5.
# Создать программу, которая будет производить подсчёт количества слов в
# каждом файле в указанной директории и выводить результаты в консоль.
# Используйте асинхронный подход.
import os
import asyncio
from pathlib import Path

file_dir = Path(Path.cwd(), 'downloads')


async def count_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        # print(f'Количество слов в файле {file_path} равно: {len(f.read().split())}')
        file_name = str(file_path).split("\\")[-1]
        word_count = len(f.read().split())
        print(f'Количество слов в файле {file_name} равно: {word_count}')


async def main():
    tasks = [asyncio.create_task(count_words(Path(file_dir, file)))
             for file in os.listdir(file_dir)
             if Path(file_dir, file).is_file()]
    asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
