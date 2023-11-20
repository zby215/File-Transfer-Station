from tkinter import *

window = Tk()
window.title('My Application')
window.geometry('200x50')

options = (1, 2, 3)
my_variable_object = IntVar()
my_variable_object.set('choose:')
my_dropdown = OptionMenu(window, my_variable_object, *options)
my_dropdown.grid()

window.mainloop()
