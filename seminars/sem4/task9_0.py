# Задание №9 - СИНХРОННАЯ
# Написать программу, которая скачивает изображения с заданных URL-адресов и
# сохраняет их на диск. Каждое изображение должно сохраняться в отдельном (файле,
# название, которого соответствует названию изображения в URL-адресе.
# Например URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
# Программа должна использовать многопоточный, многопроцессорный и асинхронный подходы.
# Программа должна иметь возможность задавать список URL-адресов через аргументы
# командной строки.
# Программа должна выводить в консоль информацию о времени скачивания каждого
# изображения и общем времени выполнения программы.

import time
from pathlib import Path

import requests
import logging

# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.basicConfig(level=logging.INFO, format='%(message)s')
loger = logging.getLogger(__name__)

start_t0 = time.time()

urls = [
    'https://remosnov.ru/wp-content/uploads/6/8/0/6806895650d56a8f74987c7d7c2d5def.jpeg',
    'https://mykaleidoscope.ru/uploads/posts/2020-10/1602832177_28-p-elementi-dekora-v-interere-38.jpg',
    'https://estatemebel.ru/wp-content/uploads/9/2/1/92183ebb46c83a64712b0065d67b004f.jpeg',
    'https://hameleone.ru/wp-content/uploads/4/8/1/4812217951a03babc907ef5e2b5c8a8e.jpeg',
    'https://mebel-complect.ru/wp-content/uploads/c/8/5/c8584dc402ee7949e1817dc922c82265.jpeg',
]

path_download = Path(Path.cwd(), 'downl_img')
if not path_download.is_dir():
    path_download.mkdir(parents=True, exist_ok=True)

for url in urls:
    start_t = time.time()
    resp = requests.get(url)
    filename = url[-11:]
    file_path = Path(path_download, filename)
    with open(file_path, 'wb') as f:
        f.write(resp.content)
        file_dl = str(filename).split("\\")[-1]
        loger.info(f'Файл {file_dl} скачан за {time.time() - start_t:.3f} сек')

loger.info(f'Всего затрачено времени {time.time() - start_t0:.3f} сек')
