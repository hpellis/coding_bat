#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 14:42:07 2018

@author: harriet
"""
#
#Given a string, return a new string where the first and last chars have been exchanged.
#
#
#front_back('code') → 'eodc'
#front_back('a') → 'a'
#front_back('ab') → 'ba'


def front_back(str):
  if len(str) == 0 or len(str) == 1:
    return str
  return str[-1] + str[1:-1] + str[0]
