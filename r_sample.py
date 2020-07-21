#! /usr/bin/env python
'''
import sys
if len(sys.argv) != 2:
    print(f"#usage: python {sys.argv[0]} [txt]")
    sys.exit()

with open(f,'r') as handle:
    if line.startswith(">"):
        continue
    else:
        print(f.strip())
'''
import json
import sys

def read_txt(file_name:str) -> str:
    ret = ""
    with open(file_name,'r') as handle:
        for line in handle:
            if lien.startswith("#"):
                continue
            ret += line.strip()
    return ret

def read_tsv(file_name: str) -> list:
    ret = []
    with open(file_name, 'r') as handle:
        for line in handle:
            if line.startswith("#"):
                header = line.strip().split("\t")
                continue
            splitted = line.strip().split("\t")
            d = dict(zip(header, splitted))
            ret.append(d)
    return ret

def to_json(l:list) -> None:
    with open("read_sample.json",'w') as handle:
        json.dump(l, handle, indent=4)

if __name__=="__main__":
    if len(sys.argv) != 2:
        print(f"#usage: python {sys.argv[0]} [txt]")
        sys.exit()

print(to_json(



