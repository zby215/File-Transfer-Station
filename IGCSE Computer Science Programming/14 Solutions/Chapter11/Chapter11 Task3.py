"""
def input_data():
    label1.config(text='')
    label2.config(text='')
    label3.config(text='')

    if int(tbox2.get()) < 0 or int(tbox2.get()) > 3:
        tbox2.delete(0, END)
        label2.config(text='Interger between 0 and 3 only')
        return
    else:
        index = int(tbox2.get())

    while True:
        try:
            data_item = int(tbox1.get())
            break
        except:
            tbox1.delete(0, END)
            label1.config(text='Integer only')
            return


task[index] = data_item


def output_data():
    label1.config(text='')
    label2.config(text='')
    label3.config(text='')

    if int(tbox3.get()) < 0 or int(tbox3.get()) > 3:
        tbox3.delete(0, END)
        label3.config(text='Integer between 0 and 3 only')
        return
    else:
        index = int(tbox3.get())

    tbox4.delete(0, END)
    tbox4.insert(END, task[index])
"""