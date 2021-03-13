#!/bin/python3

import sys


S = input().strip()
try:
    x=int(S)  #S contains a integer strings 
    print(x)
except:
    try:
        c=ord(S)
        print(c)
    except:
        print("Bad String")
