#!/usr/bin/python3.10.10
# -*- encoding: utf-8 -*-
# Copyright (C) 2023/11/20, Inc. All Rights Reserved
# @Author  :   Boyu_Zhang(Bob) 
# @Contact :   boyuzhang215@gmail.com

def circlmference(r):
    c=2*3.142*r
    return c

radius=int(input('What is the radiuse of your circle?'))

circumf=circlmference(radius)
print('The circumference of your circle is',circumf)