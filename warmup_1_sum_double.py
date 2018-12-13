# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 12:26:39 2018

@author: 612383249
"""

#Given two int values, return their sum. Unless the two values are the same, then return double their sum.
#
#
#sum_double(1, 2) → 3
#sum_double(3, 2) → 5
#sum_double(2, 2) → 8


def sum_double(a, b):
  if a != b:
    return a+b
  else:
    return (a+b) *2
