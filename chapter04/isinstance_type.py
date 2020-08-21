# -*- coding:utf-8 -*-

__author__ = "Atituset"

class A:
    pass

class B(A):
    pass

b = B()
print(isinstance(b, B))
print(isinstance(b, A))

print(type(b) is B)
print(id(type(b)) == id(B))
print(type(b) is A)
