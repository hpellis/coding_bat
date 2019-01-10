#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 11:51:42 2019

@author: harriet
"""

#Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.
#
#
#has22([1, 2, 2]) → True
#has22([1, 2, 1, 2]) → False
#has22([2, 1, 2]) → False


def has22(nums):

  for i in range (0, len(nums)-1):
    if nums[i:i+2] == [2,2]:
      return True
  
  else:
    return False