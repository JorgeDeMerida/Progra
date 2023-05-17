# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 20:51:33 2021

@author: Usuario
"""
name = input()
str(name)

def normalize(name):

    # put your code here
   
    for x in name:
        if x == "é":
           new_name = name.replace("é", "e")
        if x == "ë":
           new_name = name.replace("ë", "e")
        if x == "á":
           new_name = name.replace("á", "a")
        if x == "å":
           new_name = name.replace("å", "a")
        if x == "œ":
            new_name = name.replace("œ", "oe")
        if x == "æ":
            new_name = name.replace("æ", "ae")
        
    return new_name

print(normalize(name))
