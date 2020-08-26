# -*- coding:utf-8 -*-

__author__ = "Atituset"

a = 0

def func1():
    a = 1
    def func2():
        # nonlocal a
        # global a
        a = 2
        print("closure a:", a)
    print(f"func1 a:{a}")
    func2()
    print(f"after func2, func1_a: {a}")
func1()
print(f"global a:{a}")