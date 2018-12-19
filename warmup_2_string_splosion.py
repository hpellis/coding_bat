# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 16:29:26 2018

@author: 612383249
"""


#Given a non-empty string like "Code" return a string like "CCoCodCode".
#
#
#string_splosion('Code') → 'CCoCodCode'
#string_splosion('abc') → 'aababc'
#string_splosion('ab') → 'aab'


def string_splosion(str):
  if len(str) == 1:
    return str
  if len(str) <= 2:
    return str[0]+str[0:2]
  elif len(str) <=3:
    return str[0]+str[0:2]+str
  elif len(str) <=4:
    return str[0]+str[0:2]+str[0:3]+str
  elif len(str) <=5:
    return str[0]+str[0:2]+str[0:3]+str[0:4]+str
  else:
    return str[0]+str[0:2]+str[0:3]+str[0:4]+str[0:5]+str    
    


