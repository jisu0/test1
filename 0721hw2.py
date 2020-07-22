#!/usr/bin/env python


giveIn = str(input("giveIn base: "))
def base(giveIn):
    if giveIn == 'A':
        print("Adenine")
    elif giveIn == 'C':
        print("Cytosine")
    elif giveIn == 'G':
        print("Guanine")
    elif giveIn == 'T':
        print("Thymine")
    elif giveIn == 'U':
        print("Uracil")
    else:
        print("please input base.")
pr = base(giveIn)
print(pr)
