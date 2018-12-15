#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 15:27:28 2018

@author: harriet
"""


#You and your date are trying to get a table at a restaurant. The parameter "you" is the stylishness of your clothes, in the range 0..10, and "date" is the stylishness of your date's clothes. The result getting the table is encoded as an int value with 0=no, 1=maybe, 2=yes. If either of you is very stylish, 8 or more, then the result is 2 (yes). With the exception that if either of you has style of 2 or less, then the result is 0 (no). Otherwise the result is 1 (maybe).
#
#
#date_fashion(5, 10) → 2
#date_fashion(5, 2) → 0
#date_fashion(5, 5) → 1


def date_fashion(you, date):
  if either_at_2(you, date):
    return 0
  elif either_at_8 (you, date):
    return 2
  else:
    return 1
  
def either_at_8(you, date):
  return you >= 8 or date >= 8
  
def either_at_2(you, date):
  return you <= 2 or date <= 2
  