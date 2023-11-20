from tkinter import *


def multiply():
    number = int(textbox_input1.get())
    number2 = int(textbox_input2.get())

    textbox_output.delete(0.0, END)

    for counter in range(1, number2 + 1):
        multiple = str(number * counter) + '\n'
        textbox_output.insert(END, multiple)


window = Tk()
window.title('My App')

window.geometry('200x325')
window.configure(background='linen')

input_label = Label(window, text='Number to multiply: ', bg='linen')
input_label.grid(row=0, column=0, sticky=W)
input_label2 = Label(window, text='Number to multiply: ', bg='linen')
input_label2.grid(row=2, column=0, sticky=W)
output_label = Label(window, text='Number to multiply: ', bg='linen')
output_label.grid(row=0, column=1, sticky=E)

textbox_input1 = Entry(window, width=5)
textbox_input1.grid(row=1, column=0, sticky=NW)
textbox_input2 = Entry(window, width=5)
textbox_input2.grid(row=3, column=0, sticky=NW)

textbox_output = Text(window, height=20, width=6)
textbox_output.grid(row=1, column=1, rowspan=5, sticky=E)

multiply_button = Button(window, text='Get Multiples', command=multiply)
multiply_button.grid(row=4, column=0, sticky=W)

window.mainloop()
