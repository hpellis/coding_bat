# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 12:24:23 2018

@author: 612383249
"""


#The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
#
#
#sleep_in(False, False) → True
#sleep_in(True, False) → False
#sleep_in(False, True) → True

def sleep_in(weekday, vacation):
  return not weekday or vacation