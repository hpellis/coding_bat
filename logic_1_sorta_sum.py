#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 17:51:38 2018

@author: harriet
"""

#Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.
#
#
#sorta_sum(3, 4) → 7
#sorta_sum(9, 4) → 20
#sorta_sum(10, 11) → 21


def sorta_sum(a, b):
  if a+b >= 10 and a+b <= 19:
    return 20
  else:
    return a+b
