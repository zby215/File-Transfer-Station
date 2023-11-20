#!/usr/bin/python3.10.10
# -*- encoding: utf-8 -*-
# Copyright (C) 2023/11/20, Inc. All Rights Reserved
# @Author  :   Boyu_Zhang(Bob) 
# @Contact :   boyuzhang215@gmail.com

from tkinter import *

# Declare list globally to allow both subroutines access to it
task = [None] * 4


# Functions
def input_data():
    data_item = int(tbox1.get())
    index = int(tbox2.get())
    task[index] = data_item


def output_data():
    index = int(tbox3.get())
    tbox4.delete(0, END)
    tbox4.insert(END, task[index])


# Build th GUI
# padding is asses to some widgets:
# ipadx adds internal padding to left and right
# padx adds external padding to left and right
window = Tk()
window.title('My Application')
bg_colour = 'linen'

# Create two frame
input_frame = Frame(window, bg=bg_colour)
input_frame.grid(row=0, column=0, ipadx=5, ipady=5)
output_frame = Frame(window, bg=bg_colour)
output_frame.grid(row=0, column=1, ipadx=5, ipady=5)

# Create the labels
input_label1 = Label(input_frame, text='Data Item to Add: ', bg=bg_colour)
input_label1.grid(row=1, column=0, sticky=W)
input_label2 = Label(input_frame, text='Index to be used: ', bg=bg_colour)
input_label2.grid(row=2, column=0, sticky=W)
output_label1 = Label(input_frame, text='Index to Display: ', bg=bg_colour)
output_label1.grid(row=1, column=2, sticky=W)
output_label2 = Label(input_frame, text='Value in Index: ', bg=bg_colour)
output_label2.grid(row=2, column=2, sticky=W)

# Create the button
inputButton = Button(input_frame, text='Input', command=input_data, width=24)
inputButton.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
outputButton = Button(input_frame, text='Output', command=input_data, width=24)
outputButton.grid(row=0, column=2, columnspan=2, padx=5, pady=5)

# Create the text boxes
tbox1 = Entry(input_frame, width=10)
tbox1.grid(row=1, column=1)
tbox2 = Entry(input_frame, width=10)
tbox2.grid(row=2, column=1)
tbox3 = Entry(input_frame, width=10)
tbox3.grid(row=1, column=3)
tbox4 = Entry(input_frame, width=10)
tbox4.grid(row=2, column=3)

# start tkinter loop
window.mainloop()
