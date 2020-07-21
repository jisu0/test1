#! /usr/bin/env python

l = [3, 1, 1, 2, 0, 0, 2, 3, 3]

d = {}

for i in l:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d)
