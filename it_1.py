# -*- coding:utf-8 -*-

__author__ = "Atituset"

def main():
    for i in range(10):
        try:
            if i > 5:
                return
            print(i)
        except:
            pass


if __name__ == '__main__':
    main()