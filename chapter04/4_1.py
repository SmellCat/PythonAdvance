# -*- coding:utf-8 -*-

__author__ = "Atituset"


class Cat(object):
    def say(self):
        print("i am a cat")


class Dog(object):
    def say(self):
        print("i am a dog")

    def __getitem__(self, item):
        return 'bobby'


class Duck(object):
    def say(self):
        print("i am a Duck")

animal = Cat
animal().say()


class Animal:
    def say(self):
        print("i am a animal")


animal_list = [Cat, Dog, Duck]
for animal in animal_list:
    animal().say()

a = ['Atituiset1', "Atituiset2"]
b = ['Atituiset2', "Atituiset"]
name_tuple = ['Atituiset3', "Atituiset4"]
name_set = set()
name_set.add("Atituiset5")
name_set.add("Atituiset6")
a.extend(b)
print(a)
a.extend(name_set)
print(a)
# d = dict(a=1, b=2)
# a.extend(d)
# print(d)


class Company:
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]


company = Company(["tom", "bob", "jane"])
a.extend(company)
print(a)