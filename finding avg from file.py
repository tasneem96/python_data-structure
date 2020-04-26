# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 00:15:35 2020

@author: LENOVO
"""

# Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
fname = input("Enter file name: ")
fh = open(fname)

count = 0
total = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") :
      			count= count+1
      			i=line.find(":")
      			num = line[i+1:]
      			total+=float(num)
      
print("Average spam confidence:",total/count)
