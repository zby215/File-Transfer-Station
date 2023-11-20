# -*- coding: utf-8 -*-
# Copyright (C) 21/12/2021 17:02, Inc. All Rights Reserved
# @Author  :Boyu_Zhang(Bob)
# @Software:PyCharm
# @Email   :Boyuzhang215@gmail.com


def quick_sort(data):
    if len(data) >= 2:
        mid = data[len(data) // 2]
        left, right = [], []
        data.remove(mid)
        for num in data:
            if num >= mid:
                right.append(num)
            else:
                left.append(num)
        return quick_sort(left) + [mid] + quick_sort(right)
    else:
        return data


def my_remove_main(data_list):
    data_list.remove(min(data_list))
    data_list.remove(max(data_list))
    return data_list


if __name__ == '__main__':
    list_of_value = [int(i) for i in input("input data and split by space:").split(' ')]
    n = int(input("please enter a non-negative integer:"))
    while True:
        if n <= 0:
            n = int(input("invalid data, enter again:"))
        else:
            break
    while True:
        if len(list_of_value) <= 2 * n:
            list_of_value = [int(i) for i in input("enter number list again with more number").split(' ')]
        else:
            break
    sorted_list = quick_sort(list_of_value)
    while n > 0:
        print_list = my_remove_main(sorted_list)
        n -= 1
    print(print_list)
