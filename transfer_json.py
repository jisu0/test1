#! /usr/bin/env python

import sys
import json

def read_csv(file_name:str) -> list:
    re_c = []
    cnt = 0
    key_read = ""
    value_read = ""
    with open(file_name,'r') as handle:
        for line in handle:
            print("line", line.strip())
            if cnt %2 == 0:
                key_read = line.strip().split(",")
                cnt +=1 
                continue
            value_read = line.strip().split(",")
            d = dict(zip(key_read,value_read)) 
            re_c.append(d)
    return re_c

def write_json(l:list) -> None:
    with open(file_name,"w") as handle:
        json.dump(l,handle,indent=4)

file_name = sys.argv[1]
re_c = read_csv(file_name)
print(re_c)

