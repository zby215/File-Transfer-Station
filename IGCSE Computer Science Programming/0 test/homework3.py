# -*- coding: utf-8 -*-
# Copyright (C) 3/6/2021 1:56 PM, Inc. All Rights Reserved
# @Author  :Boyu_Zhang(Bob)
# @Software:PyCharm
# @Email   :Boyuzhang215@gmail.com

length = float(input("please type in the length of the rectangle:"))
width = float(input("please type in the width of the rectangle:"))
area = length * width
if length == width:
    print("This is a square of area:", round(area, 2))
else:
    print("This is a rectangle of area:", round(area, 2))

input("press any key to continue.")

print("""Menu
1. Music
2. History
3. Design and Technology
4. Exit
""")
num = int(input("Please enter your choice:"))
if num == 1:
    print("You chose Music")
elif num == 2:
    print("You chose History")
elif num == 3:
    print("You chose Design and Technology")
elif num == 4:
    print("Goodbye")

input("press any key to continue.")

import random

num1 = random.randint(1, 7)
num2 = random.randint(1, 7)
if num1 == num2:
    score = 2 * (num1 + num2)
    print("You threw a double ", score)
elif num1 != num2:
    score = num1 + num2
    print(score)

input("press any key to continue.")

a = 0
price = float(input("please type in the price: "))
if price >= 200:
    a = price * 0.1
    price1 = price - a
elif 100 <= price < 200:
    a = price * 0.05
    price1 = price - a
print("the finally price is £", price, "that £", a, "cheaper")


