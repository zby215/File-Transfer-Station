from tkinter import *

operator = ''
number1 = 0


def operation(op):
    global number1
    global operator
    number1 = float(textbox.get())
    operator = op
    textbox.delete(0, END)


def add():
    global operator
    operator = '+'


def minus():
    global operator
    operator = '-'


def times():
    global operator
    operator = '*'


def divide():
    global operator
    operator = '/'


def clear():
    textbox.delete(0, END)


def evaluate():
    number2 = float(textbox.get())
    textbox.delete(0, END)

    if operator == '+':
        textbox.insert(END, number1 + number2)
    elif operator == '-':
        textbox.insert(END, number1 - number2)
    elif operator == '*':
        textbox.insert(END, number1 * number2)
    elif operator == '/':
        textbox.insert(END, number1 / number2)
    else:
        textbox.insert(END, 'Error')


window = Tk()
window.title('Calculator')

textbox = Entry(window, width=20)
textbox.grid(row=0, column=0, columnspan=3)

button_add = Button(window, text='+', width=3, command=add())
button_add.grid(row=2, column=0)
button_subtract = Button(window, text='-', width=3, command=minus())
button_subtract.grid(row=2, column=1)
button_multiply = Button(window, text='*', width=3, command=times())
button_multiply.grid(row=3, column=0)
button_divide = Button(window, text='/', width=3, command=divide())
button_divide.grid(row=3, column=1)
button_equals = Button(window, text='=', width=6, command=evaluate)
button_equals.grid(row=4, column=1, columnspan=2)
button_clear = Button(window, text='CLEAR', width=6, command=clear())
button_clear.grid(row=4, column=0, sticky=W)

window.mainloop()
