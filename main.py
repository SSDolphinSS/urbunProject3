'''Рисует круг. Нашел  в инете'''
# from turtle import *
# pensize(10)
# while True:
#     forward(1)
#     right(1)
#
# exitonclick()
'''Модуль 7 работа с файлами'''
# import io
# from pprint import pprint
# name = 'text.txt'
# file = open(name, 'r', encoding='utf-8')  # r, w, a - read, write, append
# print(file.writable())
# print(file.readable())
# print(file.seekable())
# pprint(file.tell())

# file.read()
# pprint(open(name, 'r', encoding='utf-8').read())

# print(file.tell())

# print(file.read())
#
# pprint(file.read())
#
#
# print(file.tell())
# print(file.tell())
# file.close()
'''7_3'''
# name = 'text.txt'
# with open(name, encoding='utf-8') as file:
#     for line in file:
#         print(line, end='')
'''7_4'''
# print('Привет,' + 'мир!')
# print('Меня зовут %(name)s, мне %(year)s' % {'name': 'Serg', 'year':30})
# print('Я учусь в {title}{postfix} {title}'.format(title='Урбан', postfix='-university'))
# print(f'{'Urban' * 2} это супер!')
'''7.5'''
# import os

# print('Текущая директория: ', os.getcwd())
# if os.path.exists('second'): # если в тек.дер-ии есть секонд дер-ия то:
#     os.chdir('second')       # изменять дер-ию
# else:
#     os.mkdir('second')       # создать дер-ию
#     os.chdir('second')
# print('Текущая директория: ', os.getcwd())
# os.makedirs(r'third\fourth') # добавление нескольких вложенных папок
# print(os.listdir())            # список файлов в текущей дериктории
# for i in os.walk('.'):       # просмотр списка вложенных дерикторий
#     print(i)
# os.chdir(r'C:\Users\User\Desktop\Urban\pythonProject3')
# print('Текущая директория: ', os.getcwd())
# print(os.listdir())
# file = [f for f in os.listdir() if os.path.isfile(f)] # метод isfile возвращает True если он содержит файл
# dirs = [d for d in os.listdir() if os.path.isdir(d)] # метод isfile возвращает True если он содержит директорию
# print(dirs)
# print(file)
# os.startfile(file[4])  # запуск файла
# print(os.stat(file[4]).st_size)   # информация о файле и еще например размер
# os.system('pip install random2')    # запуск команд из командной строки для написания баш-скриптов

# result = {(1, 0):'a', (2, 1):'b'}
# for elem in result.items():
#   print(elem)

# info = ['1', '2', '3', '4']
# f = open('test.txt', 'a+')
# f.writelines(info)
