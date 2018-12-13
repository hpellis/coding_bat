# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 14:57:57 2018

@author: 612383249
"""

#Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.
#
#
#near_hundred(93) → True
#near_hundred(90) → True
#near_hundred(89) → False
#


n=100

def near_hundred(n):
  return near_100(n) or near_200(n)
  
def near_100(n):
  return n >= 90 and n <= 110
  
def near_200(n):
  return n >= 190 and n <= 210