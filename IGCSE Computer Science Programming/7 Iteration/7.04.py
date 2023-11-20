#!/usr/bin/python3.10.10
# -*- encoding: utf-8 -*-
# Copyright (C) 2023/11/20, Inc. All Rights Reserved
# @Author  :   Boyu_Zhang(Bob) 
# @Contact :   boyuzhang215@gmail.com

modulus_counter = 0

number = int(input('Enter your number: '))

for counter in range(2, number):
    modulus = number % counter
    if modulus == 0:
        modulus_counter = modulus_counter + 1

if modulus_counter == 0:
    print('Prime number.')
else:
    print('Not a prime number.')
