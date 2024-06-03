# Задание №5.
# Создать программу, которая будет производить подсчёт количества слов в
# каждом файле в указанной директории и выводить результаты в консоль.
# Используйте процессы.

# pip install aiofiles

import os
import asyncio
import aiofiles
import time

# MY_PATH = 'downloads'
MY_PATH = 'C:\\Users\\Algor\\Desktop\\GB\\Фреймворки Flask и FastAPI\\flask_fastAPI\\seminars\\sem4\\downloads'


async def worker(file_):
    async with aiofiles.open(file_, 'r', encoding='utf-8') as f:
        content = await f.read()
        file_name = str(file_).split("\\")[-1]
        print(f' Слов в файле {file_name} : {len(content.split())}')


async def main():
    for root, dirs, files in os.walk(MY_PATH):
        for fil in files:
            file_path = os.path.join(root, fil)
            task = asyncio.create_task(worker(file_path))
            await task


if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    print(f'Время работы: {time.time() - start:0.04f} sec')
