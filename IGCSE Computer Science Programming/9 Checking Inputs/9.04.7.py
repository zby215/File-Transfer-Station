#!/usr/bin/python3.10.10
# -*- encoding: utf-8 -*-
# Copyright (C) 2023/11/20, Inc. All Rights Reserved
# @Author  :   Boyu_Zhang(Bob) 
# @Contact :   boyuzhang215@gmail.com

from datetime import datetime


def validate_date(d):
    while True:
        try:
            return datetime.strptime(d, '%d/%m/%Y')
        except:
            d = input('Date must be in the format dd/mm/yyyy: ')


date = input('Please enter date: ')
date = validate_date(date)
