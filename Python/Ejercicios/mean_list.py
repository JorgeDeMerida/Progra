# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 14:56:55 2021

@author: PickmansMod

Given a numeric sequence at the input,
create a list in which each number will 
be a digit from this input string. Then 
use this list to calculate the arithmetic 
mean, that is, the sum of all the digits 
divided by their total count.
"""

number = str(int(input()))
list(number)

sigma = [int(x) for x in number]

count = 0
meh = 0

for n in sigma:
    if n >= 0:
        count += 1
        meh = meh + n

mean = meh/count

print(mean)
