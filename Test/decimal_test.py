# -*- coding:utf-8 -*-

__author__ = "Atituset"

from decimal import Decimal

a = Decimal('2.135').quantize(Decimal('0.00'))
b = Decimal('2.145').quantize(Decimal('0.00'))
print(a, b)