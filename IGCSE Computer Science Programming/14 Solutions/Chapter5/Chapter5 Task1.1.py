from tkinter import *

window = Tk()
window.title('My Application')

Label(window, text='Name:').grid(row=0, column=0)
my_text_box = Entry(window, width=20)
my_text_box.grid(row=0, column=1)

window.mainloop()
