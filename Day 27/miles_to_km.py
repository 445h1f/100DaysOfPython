from tkinter import *


def to_km():
    miles = float(miles_input.get())
    km =  miles * 1.6
    km_result_label.config(text=str(km))

window = Tk()
window.title('Mile to Km Converter')
window.config(padx=20, pady=20)
 
miles_input = Entry(width=10)
miles_input.grid(row=0, column=1)

miles_label = Label(text='Miles')
miles_label.grid(row=0, column=2)

is_equal_label = Label(text='is equal to ')
is_equal_label.grid(row=1, column=0)

km_result_label = Label(text='0')
km_result_label.grid(row=1, column=1)

km_label = Label(text='km')
km_label.grid(row=1, column=2)

button = Button(text='Calculate', command=to_km)
button.grid(row=2, column=1)

window.mainloop()