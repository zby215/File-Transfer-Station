# -*- coding: utf-8 -*-
# Copyright (C) 3/23/2021 2:31 PM, Inc. All Rights Reserved
# @Author  :Boyu_Zhang(Bob)
# @Software:PyCharm
# @Email   :Boyuzhang215@gmail.com

# Write a program to accept a student name,
# and the marks obtained on 10 weekly tests.
# Print the name, average mark, top three marks
# and bottom three marks.
# (Use sortedMarks = sorted (markList, reverse = True) to sort the list.)

name = input("please type in students name:")
while not (name == "Bob"):
    print("name not founded,please try again")
    name = input("please type in students name:")
if name == "Bob":
    mark_list = [12, 45, 26, 49, 156, 1, 6, 16, 15, 15]
    average = sum(mark_list) / len(mark_list)
    sorted_marks = sorted(mark_list, reverse=True)
    print("the average score is:", average)
    print("the top three marks is:", sorted_marks[0:3])
    print("the bottom three marks is:", sorted_marks[9:6:-1])

input("type Enter to continue...")

# Extend the program shown in Example 3 to find the months with
# the hottest average temperature and the coldest average temperature.
# Print the month names and relevant temperatures of these months.

month_temp = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 1, 6, 7, 8, 1, 0, 1, 2, 3, 4, 5, 6, 2, 8, 9, 3}
average = sum(month_temp) / len(month_temp)
sorted_temp = sorted(month_temp, reverse=True)
print("the hottest temp is:", sorted_temp[0])
print("the coldest temp is:", sorted_temp[-1])
#
input("type Enter to continue...")

# 5. Write a program to simulate how the top scores of several players playing
# an online game many times could be held in a list.
# (a) Define a two-dimensional list which will hold in each row, a user 10 and
# their top score for an online game. The two-dimensional list is to be
# initialised with the following values:
#    userID 	topScore
#    AAA01	      135
#    BBB01 	       87
#    CCC01    	  188
#    DDD01 	      109
# (b) Ask a user to enter their 10. Check if the user 10 is in the list.
#     If it is not found, append a new row containing the user 10 and a score of zero.
# (c) Generate a random number between 50 and 200 to represent the score for this game.
#     Locate the user. Check whether the new score is greater than the score in the list, and if so, replace it.
# (d) Print the whole list of players and scores.
#     Repeat steps b to d until a user 10 of xxx is entered.


import random

# initialize the list l
l = [['AAA01', 135],
     ['BBB01', 87],
     ['CCC01', 188],
     ['DDD01', 109]]

# enter their 'user10'
name = input('enter your name (user10): ')

# check if there is a userid 'user10'
for i in range(len(l)):
    if [i][0] != name:
        l.append(['user10', 0])
        break

# generate a random number between 50 and 200
random_list = range(50, 201)
score = random.choice(random_list)

# replace 0 with a higher score
if l[4][1] < score:
    l[4][1] = score

# print the whole list
print(l)
