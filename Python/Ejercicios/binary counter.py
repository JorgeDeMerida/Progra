# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 11:09:50 2021

@author: Usuario
"""
binary_string = ""
n = 0

while len(binary_string) <= 100:
    print("Print a random string containing 0 or 1:")
    random_string = str(input())  #aks to user for a number string

#given a string, keeps 1 or 0 and add to binary_string    
    for x in random_string:
        if (x == "0" or x == "1"):
            binary_string = binary_string + x
            n += 1
    current = n
    left = 100 - n
    
    if left <=0:
        print("Current data length is " + str(current))     
    else:
        print("Current data length is " + str(current) + "," + str(left) + " symbols left")

print("Final data string:")
print(int(binary_string))