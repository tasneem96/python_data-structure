# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 15:42:31 2020

@author: LENOVO
"""

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

sent = dict()
count = 0 
sent_emails = []
for line in handle:
    if line.startswith("From "):      
        split_line=line.split()
        sent_emails.append(split_line[1])
for sent_email in sent_emails:
    sent[sent_email]=sent.get(sent_email,0)+1

email =None
num = None

for e,n in sent.items():
    if num is None or n>num:
        email=e
        num=n
print(email,num)
        

     
 