# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 12:27:09 2018

@author: 612383249
"""


#Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.
#
#
#diff21(19) → 2
#diff21(10) → 11
#diff21(21) → 0

def diff21(n):
  if n <= 21:
    return absolute_diff(n)
  else:
    return 2 * absolute_diff(n)
    
    
def absolute_diff(n):
  return (abs(n - 21))
