#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 15:07:33 2018

@author: harriet
"""

#
#Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.
#
#
#without_end('Hello') → 'ell'
#without_end('java') → 'av'
#without_end('coding') → 'odin'


def without_end(str):
  return str[1:-1]
