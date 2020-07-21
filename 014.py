#! /usr/bin/env python
"""
word = input("Enter: ")
if word.isdigit():
    print("is digit.")
elif word.isalpha():
    print("is alpha.")
"""

word = input("Enter: ")

if word.isalpha():
    print("문자입니다.")
elif word.isnumeric():
    print("숫자입니다.")
else:
    print("??")
    
