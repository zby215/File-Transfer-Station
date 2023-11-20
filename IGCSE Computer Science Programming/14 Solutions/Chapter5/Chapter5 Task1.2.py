from tkinter import *

window = Tk()
window.title('My Application')

frame1 = Frame(window, height=20, width=100, bg='green')
frame1.grid(row=0, column=0)
frame2 = Frame(window, height=20, width=100, bg='red')
frame2.grid(row=1, column=1)

window.mainloop()
