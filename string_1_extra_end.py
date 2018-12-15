#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 15:00:45 2018

@author: harriet
"""


#Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.
#
#
#extra_end('Hello') → 'lololo'
#extra_end('ab') → 'ababab'
#extra_end('Hi') → 'HiHiHi'


def extra_end(str):
  return 3 * str[-2:]
