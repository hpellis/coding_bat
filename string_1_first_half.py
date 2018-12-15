#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 15:04:25 2018

@author: harriet
"""


#Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".
#
#
#first_half('WooHoo') → 'Woo'
#first_half('HelloThere') → 'Hello'
#first_half('abcdef') → 'abc'


def first_half(str):
  return str[0:len(str)/2]
