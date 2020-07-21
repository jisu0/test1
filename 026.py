#! /usr/bin/env python

Seq1 = "ATGTTATAG"

for i in range(0,len(Seq1),3):
    print(i, i+3, Seq1[i:i+3])

