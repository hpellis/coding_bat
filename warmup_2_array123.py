#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 14:57:12 2018

@author: harriet
"""

#Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.
#
#
#array123([1, 1, 2, 3, 1]) → True
#array123([1, 1, 2, 4, 1]) → False
#array123([1, 1, 2, 1, 2, 3]) → True

def array123(nums):
  
  for i in range(len(nums)-2):
    if nums[i:i+3] == [1,2,3]:
      return True
  return False
