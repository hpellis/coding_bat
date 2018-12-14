# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 11:07:14 2018

@author: 612383249
"""

#Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.
#
#
#pos_neg(1, -1, False) → True
#pos_neg(-1, 1, False) → True
#pos_neg(-4, -5, True) → True


def pos_neg(a, b, negative):
  if param_negative(negative) and both_negative(a,b):
    return True
  elif not param_negative(negative) and both_negative(a,b):
    return False
  elif not param_negative(negative) and only_one_negative (a,b):
    return True
  else:
    return False
    
def param_negative(negative):
  return negative
  
def both_negative(a, b):
  return a < 0 and b < 0

def only_one_negative(a,b):
  return a < 0 or b < 0