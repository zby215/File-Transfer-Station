#!/usr/bin/python3.10.10
# -*- encoding: utf-8 -*-
# Copyright (C) 2023/11/20, Inc. All Rights Reserved
# @Author  :   Boyu_Zhang(Bob) 
# @Contact :   boyuzhang215@gmail.com

number = int(input('Input number to multiply: '))

counter = 1
while counter <= 10:
    multiple = number * counter
    print(multiple)
    counter = counter + 1
