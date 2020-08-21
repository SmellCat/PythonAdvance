# -*- coding:utf-8 -*-

__author__ = "Atituset"


class Company:
    def __init__(self, employee_list):
        self.employee = employee_list

    def __len__(self):
        return len(self.employee)

com = Company(['Bobby', 'Bobby2'])
print(len(com))

# 我们在某些情况下希望判定某个对象的类型
from collections.abc import Sized
print(isinstance(com, Sized))

# 我们需要强制某个子类必须实现某些方法
# 实现了一个web框架，集成cache（redis,cache, memorycache)
# 需要设计一个抽象基类，指定子类必须实现某些方法

# 如何去模拟一个抽象基类
import abc

class CacheBase(metaclass=abc.ABCMeta):

    # def get(self, key):
    #     raise NotImplementedError # 这个实现方式只有在调用的时候才会抛出异常
    #
    # def set(self, key, value):
    #     raise NotImplementedError

    @abc.abstractmethod
    def get(self, key):
        pass

    @abc.abstractmethod
    def set(self, key, value):
        pass

class RedisCache(CacheBase):
    pass
    # def set(self, key, value):
    #     pass

# redis_cache = RedisCache() #
# redis_cache.set("key", "value")

class A:
    pass

class B(A):
    pass

b = B()
print(isinstance(b, A))