#!/usr/bin/python3.10.10
# -*- encoding: utf-8 -*-
# Copyright (C) 2023/11/20, Inc. All Rights Reserved
# @Author  :   Boyu_Zhang(Bob) 
# @Contact :   boyuzhang215@gmail.com

number1 = int(input('Enter First Number: '))

print("""
Choose one of the following option
 A for Add
 S for Subtract
 M for Multiply
 D for Divide""")
operator = input()

number2 = int(input('Enter Second Number: '))
if operator == 'A':
    print(number1 + number2)
elif operator == 'S':
    print(number1 - number2)
elif operator == 'M':
    print(number1 * number2)
elif operator == 'D':
    print(number1 / number2)
else:
    print('Incorrect Operator')
