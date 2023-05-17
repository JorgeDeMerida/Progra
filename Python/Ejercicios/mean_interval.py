# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 10:11:37 2021

@author: PickmansMod

Write the code that reads 2 numbers 
from the keyboard, a and b. As an 
output, it shows the mean of all 
numbers that lie on the interval 
between a and b, and can be divided 
by 3.
"""
a = int(input())
b = int(input()) + 1
count = 0
acu = 0

for i in range(a, b):
    if i%3 == 0:
        acu = acu + i 
        count += 1
mean = acu/count
print(mean)


    
