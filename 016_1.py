#! /usr/bin/env python

import sys
import gzip

if len(sys.argv) != 2:
    print(f"#usage: python {sys.argv[0]} [fasta.gz]")
    sys.exit()
    
f = sys.argv[1]
d = {}

with gzip.open(f, 'rb') as handle:
    for line in handle:
        line = line.decode("utf-8").strip()
        if line.startswith(">"):
            continue
        for s in line.strip():
            if s in d:
                d[s] += 1
            else:
                d[s] = 1
with open("0721result.txt", 'w') as Result:
    Result.write(f"A: {d['A']}\n")
    Result.write(f"C: {d['C']}\n")
    Result.write(f"G: {d['G']}\n")
    Result.write(f"T: {d['T']}\n")
    Result.write(f"len: {d['A']+d['C']+d['G']+d['T']}")


