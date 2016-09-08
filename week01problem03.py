# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 14:13:01 2016

@author: Dharit
"""

s = 'pcnflmqgnliyqlncynot'

subIndex = 0
subLen = 0
tSubIndex = 0
tSubLen = 0
count = 0

for i in range(len(s)-1):
    count = i
    tSubIndex = i
    while s[count]<=s[count+1]:
        count = count + 1
        if (count + 1)>=len(s):
            break
    tSubLen = count - i + 1
    if tSubLen > subLen:
        subLen = tSubLen
        subIndex = tSubIndex
print("Longest substring in alphabetical order is: " + s[subIndex:(subIndex+subLen)])