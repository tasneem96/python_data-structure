# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 19:00:32 2020

@author: LENOVO
"""

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()

time =[]
hour_list =[]
for line in handle:  
    if line.startswith("From "):
        words=line.split()
        #print(words)
        time.append(words[-2])
        for i in range(len(time)):
            hour = time[i].split(':')
        #print(hour)
        hour_list.append(hour[0])
for tm in hour_list:
    counts[tm]=counts.get(tm,0)+1

time_count= []
for k,v in counts.items():
    time_count.append((k,v))
time_count = sorted(time_count)

for k,v in time_count:
    print(k,v)
#print(time_count)
#print(counts)
#print(hour_list)

        
        
        
       
       
            
