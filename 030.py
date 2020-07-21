#! /usr/bin/env python

import sys

Seq1 = sys.argv[1]

for i in range(0,len(Seq1),1):
    if Seq1[i:i+2] == "TT":
        print(i)
        

