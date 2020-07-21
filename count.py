#!/usr/bin/env python

import sys

class FASTA:
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.count = {}
        self.length = 0
    
    def count_base(self):
        with open(self.file_name, 'r') as handle:
            for line in handle:
                if line.startswith(">"):
                    continue
                line = line.strip()
                for s in line:
                    if s in self.count:
                        self.count[s] += 1
                    else:
                        self.count[s] = 1
    
    def __len__(self):
        for k,v in self.count.items():
            self.length += v
        return self.length        

if __name__=="__main__":
    if len(sys.argv) != 2:
        print(f"#usage: python {sys.argv[0]} [fasta]")
        sys.exit()
    file_name = sys.argv[1]
    t = FASTA(file_name)
    t.count_base()
    print(t.count)
    print(len(t))


"""
import sys

f = sys.argv[1]
count_dna = {}

if len(sys.argv) != 2:
    print(f"#usage: python {sys.argv[0]} [FASTQ]")
    sys.exit()

with open(f,'r') as handle:
    for line in handle:
        if line.startswith(">"):
            continue
        for s in line.strip()
"""

