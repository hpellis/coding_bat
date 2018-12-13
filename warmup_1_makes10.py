# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 12:28:48 2018

@author: 612383249
"""

#Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
#
#
#makes10(9, 10) → True
#makes10(9, 9) → False
#makes10(1, 9) → True


def makes10 (a, b):
  return sum_10(a, b) or is_10(a, b)
  
def sum_10 (a, b):
  return a+b == 10
  
def is_10 (a, b):
  return a == 10 or b == 10
