#! /usr/bin/env python
'''
for i in range(2,10):
    if i%2 == 0:
    print("i","단")
        for j in range(1,10):
            gugu = i*j
            print("i","*","j","=",gugu)
'''
for i in range(2,10,1):
    for j in range(1,10,1):
        if i % 2 == 0:
            print(f"{i} x {j} = {i*j}")
    
