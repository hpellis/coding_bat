#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 13:53:26 2018

@author: harriet
"""

#Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.
#
#
#not_string('candy') → 'not candy'
#not_string('x') → 'not x'
#not_string('not bad') → 'not bad'


def not_string(str):
  if not no_not(str):
    return "not " + str
  else:
    return str

def no_not(str):
  if str[:3] == "not":
    return str
  