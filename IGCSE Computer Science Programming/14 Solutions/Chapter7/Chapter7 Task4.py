from tkinter import *


def prime():
    modulus_counter = 0

    number = int(textbox_input.get())

    textbox_output.delete(0.0, END)

    for counter in range(2, number):
        modulus = number % counter
        if modulus == 0:
            modulus_counter = modulus_counter + 1

    if modulus_counter == 0:
        textbox_output.insert(END, 'Prime number.')
    else:
        textbox_output.insert(END, 'Not a prime number.')


window = Tk()
window.title('My App')

window.geometry('200x50')
window.configure(background='lightgreen')

textbox_input = Entry(window, width=10)
textbox_input.grid(row=0, column=1, sticky=E)

textbox_output = Text(window, height=1, width=25)
textbox_output.grid(row=1, column=0, columnspan=2)

prime_button = Button(window, text='Prime ?', command=prime)
prime_button.grid(row=0, column=0, sticky=W)

window.mainloop()
