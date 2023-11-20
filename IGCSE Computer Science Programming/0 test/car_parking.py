#!/usr/bin/python3.10.10
# -*- encoding: utf-8 -*-
# Copyright (C) 2023/11/20, Inc. All Rights Reserved
# @Author  :   Boyu_Zhang(Bob) 
# @Contact :   boyuzhang215@gmail.com

"""
Write a program to calculate car park charges.
Up to 2 hours costs £3.50, up to 4 hours £5.00, up to 12 hours £10.00.
The driver enters the number of hours they require and the machine prints the current time, expiry time and charge.

For example:
 Wed Mar 8 15:47:46 2017
Expires: Thu Mar 9 03:47:46 2017
Charge= 10.00

Tip: Use the Python library function time by writing import time at the top of the
program. The time in seconds since January 1st 1970 is given by currentTime = time.time()
This can be formatted as shown in the sample output above with the statement:
currentTimeFormatted = time.ctime(currentTime)
"""

import datetime

fee = int()
# get the number of hours
h = int(input('please enter the number of hours you need (0-12): '))
while not (0 < h <= 12):
    print('invalid number!')
    h = int(input('please enter the number of hours you need (0-12): '))

# calculate charges
if h <= 2:
    fee = 3.50
elif 2 < h <= 4:
    fee = 5.00
elif 4 < h <= 12:
    fee = 10.00

# get time now
now = datetime.datetime.now()

# calculate the expire time
delta = datetime.timedelta(hours=h)
end = now + delta

# output
print('Time now: ', now.strftime('%Y-%m-%d %H:%M:%S'))
print('Expires:', end.strftime('%Y-%m-%d %H:%M:%S'))
print('Charge = £', fee)
