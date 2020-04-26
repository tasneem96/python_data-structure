# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 23:26:16 2020

@author: LENOVO
"""

largest = -1
smallest =10000
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        n=int(num)
        
    except:
        print("Invalid input")
    if n > largest:
        largest = n 
    if n<smallest :
        smallest = n
print("max" ,largest)
print("min" , smallest)
   
    

