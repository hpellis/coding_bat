#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 15:25:46 2018

@author: harriet
"""

#Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.
#
#
#string_match('xxcaazz', 'xxbaaz') → 3
#string_match('abc', 'abc') → 2
#string_match('abc', 'axc') → 0

def string_match(a, b):

  if len(a) > len(b):
    length=len(b)
  else:
    length=len(a)
    
  count=0
    
  for i in range (length-1):
    a_substr=a[i:i+2]
    b_substr=b[i:i+2]
    
    if a_substr == b_substr:
      count+= 1
      
  return count