#!/usr/bin/python3.10.10
# -*- encoding: utf-8 -*-
# Copyright (C) 2023/11/20, Inc. All Rights Reserved
# @Author  :   Boyu_Zhang(Bob) 
# @Contact :   boyuzhang215@gmail.com

def button_click():
    if text_box.get() == '':
        my_label.config(text='Enter text here: ')
    else:
        user_input = text_box.get()