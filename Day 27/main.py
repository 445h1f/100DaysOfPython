from tkinter import *


window = Tk()
window.title('My first GUI App')
window.minsize(width=400, height=200)

def onclick():
    my_label.config(text=input.get())


my_label = Label(text='My Label')
my_label.grid(row=0, column=0)


my_button = Button(text='Click Me', command=onclick)
my_button.grid(row=1, column=1)

button_2 = Button(text='2nd Button')
button_2.grid(row=0, column=2)
input = Entry(width=10)
input.grid(row=3, column=3)


window.mainloop()