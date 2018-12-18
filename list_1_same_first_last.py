# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 16:05:15 2018

@author: 612383249
"""

#Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.
#
#
#same_first_last([1, 2, 3]) → False
#same_first_last([1, 2, 3, 1]) → True
#same_first_last([1, 2, 1]) → True


def same_first_last(nums):
  return len(nums) >= 1 and first_last_equal(nums)
  
def first_last_equal(nums):
  return nums[0] == nums[-1]
