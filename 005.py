#! /usr/bin/env python

num1 = 21
if num1%3 == 0 and num1%7 ==0:
    print("3의 배수, 7의 배수")
elif num1%3 == 0:
    print("3의 배수")
elif num1%7 == 0:
    print("7의 배수")
else:
    print("3의 배수도, 7의 배수도 아님")

