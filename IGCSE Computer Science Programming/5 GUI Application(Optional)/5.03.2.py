#!/usr/bin/python3.10.10
# -*- encoding: utf-8 -*-
# Copyright (C) 2023/11/20, Inc. All Rights Reserved
# @Author  :   Boyu_Zhang(Bob) 
# @Contact :   boyuzhang215@gmail.com

from tkinter import *


def change_text():
    my_label.config(text=gender.get())


window = Tk()
window.title('My Application')

my_label = Label(window, width=25, height=1, text='')
my_label.grid(row=0, column=0)

my_button = Button(window, text='Submit', width=10, command=change_text)
my_button.grid(row=1, column=0)

gender = StringVar()

radio1 = Radiobutton(window, text='Female', variable=gender, value='Female')
radio1.grid(row=2, column=0, sticky=W)
radio1.select()
radio2 = Radiobutton(window, text='Male', variable=gender, value='Male')
radio2.grid(row=3, column=0, sticky=W)

window.mainloop()
