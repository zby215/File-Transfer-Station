from tkinter import *

operator = ''
number1 = 0


def operation(op):
    global number1
    global number2
    global operator

    if operator == '':
        number1 = float(textbox.get())
    else:
        number2 = float(textbox.get())
        if operator == '+':
            answer = number1 + number2
        elif operator == '-':
            answer = number1 - number2
        elif operator == '*':
            answer = number1 * number2
        elif operator == '/':
            answer = number1 / number2

        textbox.delete(0, END)
        textbox.insert(END, answer)

        number1 = float(answer)
        operator = op


def add():
    operation('+')


def minus():
    operation('-')


def times():
    operation('*')


def divide():
    operation('/')


def clear():
    global operator
    global number1
    global number2

    textbox.delete(0, END)
    operator = ''
    number1 = 0.0
    number2 = 0.0


def evaluate():
    global operator
    global number1
    global number2

    number2 = float(textbox.get())

    textbox.delete(0, END)

    if operator == '+':
        answer = number1 + number2
    elif operator == '-':
        answer = number1 - number2
    elif operator == '*':
        answer = number1 * number2
    elif operator == '/':
        answer = number1 / number2
    else:
        answer = (END, 'Error')

    textbox.insert(END, answer)
    operator = ''
