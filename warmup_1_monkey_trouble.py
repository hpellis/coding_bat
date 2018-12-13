# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 12:25:40 2018

@author: 612383249
"""


#We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.
#
#
#monkey_trouble(True, True) → True
#monkey_trouble(False, False) → True
#monkey_trouble(True, False) → False


def both_smiling(a_smile, b_smile):
  return a_smile and b_smile
  
def neither_smiling(a_smile, b_smile):
  return not a_smile and not b_smile
  
  
def monkey_trouble(a_smile, b_smile):
  return both_smiling(a_smile, b_smile) or neither_smiling(a_smile, b_smile)
 

   
