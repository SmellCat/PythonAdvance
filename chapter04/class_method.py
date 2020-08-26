# -*- coding:utf-8 -*-

__author__ = "Atituset"


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def tomorrow(self):
        self.day += 1

    @staticmethod
    def parse_from_string(date_str):
        year, month, day = tuple(date_str.split('-'))
        return Date(int(year), int(month), int(day))

    @classmethod
    def from_string(cls, date_str):
        year, month, day = tuple(date_str.split('-'))
        return cls(int(year), int(month), int(day))

    def __str__(self):
        return "{year}/{month}/{day}".format(year=self.year, month=self.month, day=self.day)


if __name__ == '__main__':
    new_day = Date(2020, 8, 26)
    new_day.tomorrow()
    print(new_day)

    date_str = '2020-8-27'
    year, month, day = tuple(date_str.split('-'))
    new_day = Date(int(year), int(month), int(day))
    print(new_day)

    # 用staticmethod完成初始化
    new_day = Date.parse_from_string('2020-8-27')
    print(new_day)

    # 用classmethod完成初始化
    new_day = Date.from_string('2020-8-27')
    print(new_day)