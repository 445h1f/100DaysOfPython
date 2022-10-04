from tkinter import *

window = Tk()
window.title('Testing')
window.config(padx=20, pady=20)

data = {
    'One' : 0,
    'Two' : 0,
    'Three' : 0,
    'Four' : 0,
    'Five' : 0,
    'Six' : 0,
    'Seven' : 0
}
label_text = ''
for i in data:
    label_text += f'{i}: {data[i]}\n'

main_label = Label(text=label_text, font=('Fira Code', 18, 'bold'))
main_label.pack()
window.mainloop()