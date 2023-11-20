#!/usr/bin/python3.10.10
# -*- encoding: utf-8 -*-
# Copyright (C) 2023/11/20, Inc. All Rights Reserved
# @Author  :   Boyu_Zhang(Bob) 
# @Contact :   boyuzhang215@gmail.com

def teamMembers(*names):
    members = ['Bob', 'Marry', 'James', 'Kelly']
    i = 0
    for name in names:
        members[i] = name
        i = i + 1

    print('The team members are {}, {}, {} and {}.'.format(members[0], members[1], members[2], members[3]))


if __name__ == '__main__':
    teamMembers('Joanne', 'Lee')
    teamMembers('Benny', 'Aaron')
    teamMembers('Peter', 'John', 'Ben')
    teamMembers('Jammy', 'Adam', 'Calvin', 'Denny')
