# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 23:57:31 2020

@author: LENOVO
"""

#7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.
fname = input("Enter file name: ")
try:
   fh = open(fname)
except:
    print("{} file can't open".format(fname))
    quit()
for line in fh:
    f=line.strip()
    print(f.upper())

    
    