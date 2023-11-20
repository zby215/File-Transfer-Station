#!/usr/bin/python3.10.10
# -*- encoding: utf-8 -*-
# Copyright (C) 2023/11/20, Inc. All Rights Reserved
# @Author  :   Boyu_Zhang(Bob) 
# @Contact :   boyuzhang215@gmail.com

day = int(input('Enter the day of the month: '))

while day < 1 or day > 31:
    day = int(input('Enter a value between 1 and 31: '))
