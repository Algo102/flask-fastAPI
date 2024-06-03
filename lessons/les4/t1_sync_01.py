import time


def count_down(n):
    for i in range(n, 0, -1):
        print(i)
        time.sleep(1)  # программа засыпает на 1 секунду,
        # вместо sleep может быть какойто процесс программы


count_down(5)
