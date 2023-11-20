#!/usr/bin/python3.8.2
# -*- coding: utf-8 -*-
# Copyright (C) 2/27/2021, Inc. All Rights Reserved
# @Author  : Boyu_Zhang(Bob)
# @Email   : Boyuzhang215@gmail.com

food = input("please type in your favourite food: ")
color = input("please type in your favourite color: ")
print("My favourite food is " + food + " and my favourite color is " + color)
print("My favourite food is", food, "and my favourite color is", color, "\n")

input("Press \"Enter\" to continuous")

name = input("please type in your name: ")
telephone_number = input("please type in your telephone number: ")
print(name, '\n')
print(telephone_number)
print(name, '\t', telephone_number)

input("Press \"Enter\" to continuous")

a = int(40 / 11)
print(a)

input("Press \"Enter\" to continuous")

b = int(40 % 11)
print(b)

input("Press \"Enter\" to continuous")

c = int(2 ** 10)
print(c)

input("Press \"Enter\" to continuous")

if 3 > 2:
    print("3 is bigger than 2")

input("Press \"Enter\" to continuous")

string1 = 'abc'
string2 = 'ABC'
if string1.lower() < string2.lower():
    print("abc is smaller than ABC")
else:
    print("abc is not smaller than ABC")

input("Press \"Enter\" to continuous")

if 1 <= 4 and 7 <= 7:
    print("true")

input("Press \"Enter\" to continuous")

string1 = 'Fred'
string2 = 'fred'
if string1.lower() == string2.lower():
    print("Fred is equal to fred")
else:
    print("Fred is not   equal to fred")

input("Press \"Enter\" to finish.")
