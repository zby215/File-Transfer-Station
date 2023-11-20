#!/usr/bin/python3.10.10
# -*- encoding: utf-8 -*-
# Copyright (C) 2023/11/20, Inc. All Rights Reserved
# @Author  :   Boyu_Zhang(Bob) 
# @Contact :   boyuzhang215@gmail.com

from tkinter import *

window = Tk()
window.title('My Application')

window.mainloop()

Label(window, text='Name:').grid(row=0, column=0)
my_text_box = Entry(window, width=15)
my_text_box.grid(row=0, column=1)

frame1 = Frame(window, height=20, width=100, bg='green')
frame1.grid(row=0, column=0)
frame2 = Frame(window, height=20, width=100, bg='red')
frame2.grid(row=1, column=1)

options = (1, 2, 3)
my_variable_object = IntVar()
my_variable_object.set('choose:')
my_dropdown = OptionMenu(window, my_variable_object, *options)
my_dropdown.grid()
