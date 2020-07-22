#! /usr/bin/env python

'''
try:
    n = int(input("number: "))
    print(10/n)
except ZeroDivisionError:
    print("0 이외의 숫자를 입력하세요.")
'''

def divNum(n):
    try:
        val_dN = 10/n
    except ZeroDivisionError:
        val_dN = "0이외의 숫자를 입력하세요."
    return val_dN

n = int(input("number: "))
print(divNum(n))



