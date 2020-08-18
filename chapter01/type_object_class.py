# -*- coding:utf-8 -*-

__author__ = "Atituset"

a = 1
b = 'abc'
print(type(1))
print(type(int))
print(int.__bases__)
print(type(b))
print(type(str))

# object是最顶层的类
# type也是一个类，同时type也是一个对象

class Student:
    pass

stu = Student()
print(type(stu))
print(type(Student))
print(Student.__bases__)

class MyStudent(Student):
    pass

print(MyStudent.__bases__)

print(type.__bases__)
print(object.__bases__)
print(type(object))
