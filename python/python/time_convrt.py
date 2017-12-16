#!/bin/python3

import sys

def timeConversion(s):
    l=s.split(':')
    s1=''
    h=int(l[0])+12
    if l[2][2:]=='AM':
        if h!=24:
            s1=s[:8]
        elif h==24:
            l[0]='00'
            s1=l[0]+':'+l[1]+':'+l[2][:2]
    else:
        if h!=24:
            l[0]=str(h)
            s1=l[0]+':'+l[1]+':'+l[2][:2]
        elif h==24:
            s1=s[:8]
    return s1

s = input().strip()
result = timeConversion(s)
print(result)

