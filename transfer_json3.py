#!/usr/bin/env python
import sys
import json

def read_csv(file_name : str) -> list :
    ret = []
    d = {}
    cnt = 0
    first = ""
    second = ""

    with open(file_name, 'r') as handle :
        for line in handle :
            if cnt % 2 == 0 :
                first = line.strip().split(",")
            elif cnt % 2 != 0 :
                second = line.strip().split(",")
            cnt += 1
            d = dict(zip(first, second))
            ret.append(d)
    return ret

def to_json(l: list, file_name : str) -> None :
    with open(file_name, 'w') as handle :
        json.dump(l, handle, indent = 4) # dump : 파이썬 타입을 json으로 변환

file_name = sys.argv[1]
ret = read_csv(file_name)
to_json(ret, "programing2_result.json")
