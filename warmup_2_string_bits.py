# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 11:47:40 2018

@author: 612383249
"""

#Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
#
#
#string_bits('Hello') → 'Hlo'
#string_bits('Hi') → 'H'
#string_bits('Heeololeo') → 'Hello'


def string_bits(str):
  return str[::2]
