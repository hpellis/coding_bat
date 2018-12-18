# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 16:08:54 2018

@author: 612383249
"""


#Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more.
#
#
#common_end([1, 2, 3], [7, 3]) → True
#common_end([1, 2, 3], [7, 3, 2]) → False
#common_end([1, 2, 3], [1, 3]) → True

def common_end(a, b):
  return first_element_equal(a,b) or last_element_equal(a,b)

def first_element_equal(a,b):
  return a[0] == b[0]
  
def last_element_equal(a,b):
  return a[-1] == b[-1]
