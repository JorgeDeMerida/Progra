# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 16:55:21 2021

@author: Usuario
"""

name = input()
str(name)

def normalize(name):

    # put your code here
    latin = ""
    for x in name:
        if x == "é":
            latin = latin + "e"
        if x == "ë":
            latin = latin + "e"
        if x == "á":
            latin = latin + "a"
        if x == "å":
            latin = latin + "a"
        if x == "œ":
            latin = latin + "oe"
        if x == "æ":
            latin = + "ae"
        
        latin = latin + x
        latin = latin.strip("éëáåœæ")
        
    return latin

print(normalize(name))

