from tkinter import *

def change_text():
    my_label.config(text=gender.get())

window = Tk()
window.title('My Application')

my_label = Label(window, width=25, height=1, text='')
my_label.grid(row=0, column=0)

my_button = Button(window, text='Submit', width=10, command=change_text)
my_button.grid(row=1, column=0)

gender = StringVar()

options = ('female', 'male')
gender.set('chooses:')
my_dropdown = OptionMenu(window, gender, *options)
my_dropdown.grid()

window.mainloop()
