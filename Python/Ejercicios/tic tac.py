# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 23:27:19 2021

@author: Usuario
"""

print("Enter cells:")
cells = str(input())
cells = cells.upper()
list(cells)


#divide cells en 3 lineas con 3 elementos
first_line = cells[0:3]
second_line = cells[3:6]
third_line = cells[6:9]


#añade espacios entre cada simbolo de cada una de las listas
first_line = first_line.replace("", " ")
second_line = second_line.replace("", " ")
third_line = third_line.replace("", " ")


print(" ---------")
print("| " + first_line + " |")
print("| " + second_line + " |")
print("| " + third_line + " |")
print(" ---------")
