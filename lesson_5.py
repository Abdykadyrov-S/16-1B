"""
Декомпозиция - деленеие кода по модулям
"""


"""
Модули - все файлы с расширением .py

"""


"""
Кастомные модули:

lesson_5.py , calc.py, main.py

"""


"""
Встроенные (вложенные, библиотеки) модули:

random, time

"""

# import random
# # from random import *

# numbers = [1,2,3,4,5,6,7]

# res = random.choice(numbers)
# print(res)

# import time

# while True:
#     time.sleep(2)
#     print("loading...")


"""
Внешние модули 

termcolor

"""

from termcolor import cprint

print("Hello World!")


cprint("Hello World!", color="light_red", on_color="on_yellow")