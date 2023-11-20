#!/usr/bin/python3.10.10
# -*- encoding: utf-8 -*-
# Copyright (C) 2023/11/20, Inc. All Rights Reserved
# @Author  :   Boyu_Zhang(Bob) 
# @Contact :   boyuzhang215@gmail.com

# coding: UTF-8
'''
created on 21st Jan 2021 16:04
@author: T. Zhang
based on the code in the text book Cambridge IGCSE and O Level Programming Book
'''

# initialise the empty arrays
names = [None] * 30
squad_shots = [None] * 30
squad_assists = [None] * 30
squad_goals = [None] * 30
success_index = [None] * 30

# initialise global variables
squad_total = 0
success_highest = 0
player_highest = ''


# validation function
def validate_score(score, score_type):
    # test for integer
    try:
        int(score)
    except:
        return False

    # range test
    if score_type == 1 and (int(score) > 100 or int(score) < 0):
        return False
    if score_type == 2 and (int(score) > 50 or int(score) < 0):
        return False
    if score_type == 3 and (int(score) > 40 or int(score) < 0):
        return False

    # pass test
    return True


# Main loop
for i in range(3):
    # get inputs and validation all numerical data
    name = input('Enter player\'s name: ')
    names[i] = name

    shots = input('Enter shots made: ')
    while validate_score(shots, 1) is False:
        print('Error: Unexpected input')
        shots = input('Enter shots made: ')

    assists = input('Enter assists made: ')
    while validate_score(assists, 2) is False:
        print('Error: Unexpected input')
        assists = input('Enter assists made: ')

    goals = input('Enter goals made: ')
    while validate_score(goals, 3) is False:
        print('Error: Unexpected input')
        goals = input('Enter goals made: ')

    # load the arrays
    squad_shots[i] = int(shots)
    squad_assists[i] = int(assists)
    squad_goals[i] = int(goals)

    # process scores
    success_index[i] = squad_assists[i] + 2 * squad_shots[i] + 3 * squad_goals[i]
    squad_total = squad_total + success_index[i]

    # print current player's success_index
    print(name, success_index[i])

    # keep track of highest scoring player
    if success_index[i] > success_highest:
        success_highest = success_index[i]
        player_highest = name

# calculate squad average
squad_average = squad_total / 30

# print final summary
print('\nSquad average: ', squad_average)
print('Most successful player: ', player_highest, 'with', success_highest)
