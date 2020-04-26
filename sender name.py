# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 02:25:31 2020

@author: LENOVO
"""

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    if line.startswith("From "):
        count+=1
        split_line=line.split()
        print(split_line[1])



print("There were", count, "lines in the file with From as the first word")
