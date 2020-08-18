# -*- coding:utf-8 -*-

__author__ = "Atituset"


def ask(name="Atituset"):
    print(name)


class Person:
    def __init__(self):
        print('Atituiset1')


def print_type(item):
    print(type(item))


def decorator_func():
    print('dec start')
    return ask


my_ask = decorator_func()
my_ask('tom')

# obj_list = []
# obj_list.append(ask)
# obj_list.append(Person)
# for item in obj_list:
#     print(item())

# my_func = ask
# my_func('Atituset')
#
# my_class = Person
# my_class()