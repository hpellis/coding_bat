#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 14:43:06 2018

@author: harriet
"""


#Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.
#
#
#array_front9([1, 2, 9, 3, 4]) → True
#array_front9([1, 2, 3, 4, 9]) → False
#array_front9([1, 2, 3, 4, 5]) → False

def array_front9(nums):
  
  length=len(nums)
  if length > 4:
    length = 4
    
  for i in range(length):
    if nums[i] == 9:
      return True
      
  return False
  
