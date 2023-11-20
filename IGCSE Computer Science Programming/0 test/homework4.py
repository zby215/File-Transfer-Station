# -*- coding: utf-8 -*-
# Copyright (C) 3/11/2021 6:23 PM, Inc. All Rights Reserved
# @Author  :Boyu_Zhang(Bob)
# @Software:PyCharm
# @Email   :Boyuzhang215@gmail.com

import random

b = 0
total = 0
while b < 10:
    a = random.randint(1, 10)
    total = total + a
    b += 1
    print("the number is", a, "and the total is:", total)

input("type Enter to continue")

b = 0
total = 0
while b < 1000:
    a = random.randint(1, 10)
    total = total + a
    b += 1
average = total / 1000
print("the average number is:", average)

input("type Enter to continue")

find1 = "AB"
find2 = "00"
while True:
    a = input("please type in the 2 letters and 3 number:")
    result1 = find1 in a
    result2 = find2 in a
    if result1 == True and result2 == True:
        print("the product is", a)
        break

input("type Enter to continue")

num1 = float(input('please type in a number'))
num2 = float(input('please type in a number'))
num3 = float(input('please type in a number'))
num4 = float(input('please type in a number'))
num5 = float(input('please type in a number'))
num6 = float(input('please type in a number'))
num7 = float(input('please type in a number'))
num8 = float(input('please type in a number'))
num9 = float(input('please type in a number'))
num10 = float(input('please type in a number'))
max_num = num1
if max_num < num2:
    max_num = num2
if max_num < num3:
    max_num = num3
if max_num < num4:
    max_num = num4
if max_num < num5:
    max_num = num5
if max_num < num6:
    max_num = num6
if max_num < num7:
    max_num = num7
if max_num < num8:
    max_num = num8
if max_num < num9:
    max_num = num9
if max_num < num10:
    max_num = num10
print("the biggest number is", max_num)
