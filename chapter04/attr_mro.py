# -*- coding:utf-8 -*-

__author__ = "Atituset"

class A:
    name = "A"
    def __init__(self):
        self.name = 'obj'

# C3算法
a = A()
print(a.name)

class D:
    pass

class C(D):
    pass

class B(D):
    pass

class A(B, C):
    pass

print(A.__mro__)