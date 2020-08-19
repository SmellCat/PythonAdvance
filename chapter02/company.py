# -*- coding:utf-8 -*-

__author__ = "Atituset"


class Company:
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]

    # def __len__(self):
    #     return len(self.employee)
    def __str__(self):
        return ",".join(self.employee)

    def __repr__(self):
        return ",".join(self.employee)


company = Company(["tom", "bob", "jane"])

emploee = company.employee
for em in emploee:
    print(em)

# 加了__getitem__后可以直接这么循环
for em in company:
    print(em)

company1 = company[:2]

for em in company1:
    print(em)

print(len(company1)) # __len__ 不设置，设置了__getitem__一样可以使用