#!/usr/bin/python3.10.10
# -*- encoding: utf-8 -*-
# Copyright (C) 2023/11/20, Inc. All Rights Reserved
# @Author  :   Boyu_Zhang(Bob) 
# @Contact :   boyuzhang215@gmail.com

multiplier = 1
total = 0

isbn = input('Input an ISBN-13 number with no spaces: ')

check_digit = int(isbn[12])

for i in range(12):
    total = total + (int(isbn[i]) * multiplier)
    if multiplier == 1:
        multiplier = 3
    else:
        multiplier = 1

remainder = total % 10

if (10 - remainder) == check_digit:
    print('ISBN valid')
else:
    print('Invalid ISBN number')
