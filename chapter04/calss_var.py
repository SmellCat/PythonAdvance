# -*- coding:utf-8 -*-

__author__ = "Atituset"

class A:
    aa = 1

    def __init__(self, x, y):
        self.x = x
        self.y = y

a = A(2, 3)
A.aa = 11
a.aa = 100
a.b = 1000
print(a.x, a.y, a.aa, a.b)
print(A.aa)

