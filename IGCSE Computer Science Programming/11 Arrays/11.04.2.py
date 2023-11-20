#!/usr/bin/python3.10.10
# -*- encoding: utf-8 -*-
# Copyright (C) 2023/11/20, Inc. All Rights Reserved
# @Author  :   Boyu_Zhang(Bob) 
# @Contact :   boyuzhang215@gmail.com

def search():
    letters = ['a', 'b', 'c', 'd', 'e', 'f']

    user_letter = input('Enter the character to search for: ')

    for i in range(0, 6):
        if user_letter == letters[i]:
            print('Match found.')
            return
    print('No match.')


search()
