#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 11:48:25 2019

@author: harriet
"""


#Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.
#
#
#lucky_sum(1, 2, 3) → 6
#lucky_sum(1, 2, 13) → 3
#lucky_sum(1, 13, 3) → 1

def lucky_sum(a, b, c):
  letters=[a,b,c]
  flag = False
  for i,v in enumerate(letters):
    if v == 13 or flag == True:
      letters[i] = 0
      flag = True

  return sum(letters)
    