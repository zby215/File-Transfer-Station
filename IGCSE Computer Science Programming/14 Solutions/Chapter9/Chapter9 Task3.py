from tkinter import *


def validate_size():
    if int(entry_box.get()) < 0:
        error_label.config(text='Positive number only')
        entry_box.delete(0, END)
    elif int(entry_box.get()) > 1000:
        error_label.config(text='Must be less than 1000')
        entry_box.delete(0, END)

    return int(entry_box.get())


window = Tk()
window.title('My App')

error_label = Label(window, width=25, height=1, text='')
error_label.grid(row=1, column=0)

entry_box = Entry(window, width=5)
entry_box.grid(row=0, column=0)

submit_button = Button(window, text='Submit Number', command=validate_size)
submit_button.grid(row=2, column=0)

window.mainloop()
