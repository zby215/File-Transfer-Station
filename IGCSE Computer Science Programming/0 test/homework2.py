# -*- coding: utf-8 -*-
# Copyright (C) 3/1/2021 4:00 PM, Inc. All Rights Reserved
# @Author  :Boyu_Zhang(Bob)
# @Software:PyCharm
# @Email   :Boyuzhang215@gmail.com

proverb = "A picture's worth a thousand words"
print(proverb)
print(proverb.replace("picture's", "An image is"))
print(proverb.find("o"))
proverb_Upper = proverb.upper()
print(proverb_Upper)
print(proverb.count(str()))

input("please type enter to continue")

r = int(input("please type in the radius of the circle:"))
PI = 3.14159
area = PI * (r ** 2)
circumference = 2 * PI * r
print("the area of the circle is:", area)
print("the circumference of the circle is:", circumference)

input("please type enter to continue")

num1 = float(input("please type in a float number:"))
num2 = float(input("please type in a float number:"))
print("The sum of", num1, "and", num2, "is:", round(num1 + num2, 2))
print("The product of", num1, "and", num2, "is:", round(num1 * num2, 3))

input("Press \"Enter\" to finish.")
