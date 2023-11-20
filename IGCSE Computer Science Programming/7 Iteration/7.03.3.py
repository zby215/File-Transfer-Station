#!/usr/bin/python3.10.10
# -*- encoding: utf-8 -*-
# Copyright (C) 2023/11/20, Inc. All Rights Reserved
# @Author  :   Boyu_Zhang(Bob) 
# @Contact :   boyuzhang215@gmail.com

from tkinter import *


def multiply():
    number = int(textbox_input.get())
    textbox_output.delete(0.0, END)

    for counter in range(1, 11):
        multiple = str(number * counter) + '\n'
        textbox_output.insert(END, multiple)


window = Tk()
window.title('My App')

window.geometry('150x350')
window.configure(background='linen')

input_label = Label(window, text='number: ', bg='linen')
input_label.grid(row=0, column=0)
output_label = Label(window, text='\nOutput', bg='linen')
output_label.grid(row=2, column=0)

textbox_input = Entry(window, width=5)
textbox_input.grid(row=1, column=0)

textbox_output = Text(window, height=15, width=6)
textbox_output.grid(row=3, colume=0)

multiply_bottom = BOTTOM(window, text='Multiply', command=multiply)
multiply_bottom.grid(row=1, column=1)

window.mainloop()
