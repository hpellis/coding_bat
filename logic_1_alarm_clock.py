#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 17:51:57 2018

@author: harriet
"""


#Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation, return a string of the form "7:00" indicating when the alarm clock should ring. Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00". Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".
#
#
#alarm_clock(1, False) → '7:00'
#alarm_clock(5, False) → '7:00'
#alarm_clock(0, False) → '10:00'

def alarm_clock(day, vacation):
  if weekday(day):
    return weekday_alarm(vacation)
  else:
    return weekend_alarm(vacation)
    
def weekday(day):
  return day >=1 and day <= 5
  
def weekday_alarm (vacation):
  if vacation:
    return "10:00"
  else:
    return "7:00"

def weekend_alarm (vacation):
  if vacation:
    return "off"
  else:
    return "10:00"

    