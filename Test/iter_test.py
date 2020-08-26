# -*- coding:utf-8 -*-

__author__ = "Atituset"

l = iter('abc')
print(next(l))


class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            self.start += 1
            return self.start - 1
        else:
            raise StopIteration


# iter接收函数
# iter(函数, 参数)时，会不断执行函数func, 直到返回值与参数相同或者StopIteration
it = iter([1, 2, 3, 4, 5])


def func():
    return next(it)


class Next:
    def __init__(self):
        self.data = [0, 1, 2, 3, 4]
        self._iter = iter(self.data)

    def getLen(self):
        return len(self.data)

    def __iter__(self):
        print('iter')
        return self

    def __call__(self):
        return next(self._iter)

    def __next__(self):
        print('I am next')
        return next(self._iter)


if __name__ == '__main__':

    # for i in MyRange(1, 3):
    #     print(i)
    #
    # for i in range(1, 3):
    #     print(i)

    # for j in iter(func, 4):
    #     print(j)
    for it in iter(Next(), 6):
        print(it)