#! /usr/bin/env python
'''
with open("read_sample.txt", 'r') as handle:
    for line in handle:
        if line.startswith(">"):
            continue    #header 프린트 안되게
        print(line.strip())
'''
'''
import sys
f = sys.argv[1]     
#argv 이용하면 파일 명을 일일이 들어가서 바꿀 필요 없이 실행할 때 이용할 수 있다.

with open(f, 'r') as handle:
    for line in handle:
        if line.startswith(">"):
            continue    #header 프린트 안되게
        print(line.strip())
'''

import sys

if len(sys.argv) != 2:
    print(f"#usage: python {sys.argv[0]} [fasta]")
    sys.exit()

f = sys.argv[1]
d = {}     

with open(f, 'r') as handle:
    for line in handle:
        if line.startswith(">"):
            continue
        for s in line.strip():
            if s in d:
                d[s] += 1
            else:
                d[s] = 1
total = 0
for k,v in d.items():
    total += v

with open("result_covid.txt","w") as f1:
    f1.write(f"A: {d['A']}\n")
    f1.write(f"C: {d['C']}\n")
    f1.write(f"G: {d['G']}\n")
    f1.write(f"T: {d['T']}\n")





