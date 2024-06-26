# -*- coding: utf-8 -*-

from threading import Thread
from time import sleep


def numbers_print(start, end, interval=1, time_interval=1):
    for i in range(start, end + 1, interval):
        print(i)
        sleep(time_interval)


def letters_print(start, end, interval=1, time_interval=1):
    for i in range(start, end + 1, interval):
        print(chr(i))
        sleep(time_interval)


# Объявляем потоки
numbers_thread = Thread(target=numbers_print, args=(1, 10, 1, 1))
letters_thread = Thread(target=letters_print, args=(0x61, 0x6a, 1, 1))
# Запускаем потоки
numbers_thread.start()
sleep(0.1)  # Чтобы два потока не накладывались друг на друга
letters_thread.start()
# Ожидаем окончания потоков
numbers_thread.join()
letters_thread.join()
print('------------- The End -------------')
