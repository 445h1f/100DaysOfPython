from tkinter import *
from tkinter import messagebox
import pyperclip
import random
import json
from datetime import datetime
# ---------------------------- PASSWORD GENERATOR 
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_random_password():
    num_letters = random.randint(8, 10)
    num_symbols = random.randint(2, 5)
    num_numbers = random.randint(2, 5)

    password_letters = [random.choice(LETTERS) for _ in range(num_letters)]
    password_numbers = [random.choice(NUMBERS) for _ in range(num_numbers)]
    password_symbols = [random.choice(SYMBOLS) for _ in range(num_symbols)]

    random_password_list = password_letters + password_numbers + password_symbols
    random.shuffle(random_password_list)

    random_password = ''.join(random_password_list)
    password_input.delete(0, END)
    password_input.insert(0, random_password)
    pyperclip.copy(random_password)


# ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
FILENAME = 'password_data.json'

def reset_fields():
    email_input.delete(0, END)
    website_input.delete(0, END)
    password_input.delete(0, END)
    email_input.insert(0, 'username@gmail.com')


def get_data():
    with open(FILENAME, 'r') as data_file:
        json_data = json.load(data_file)
        return json_data

def save_data(new_data):
    with open(FILENAME, 'w') as data_file:
        json.dump(new_data, data_file, indent=4)

def save_password():
    website = website_input.get().lower()
    email = email_input.get().lower()
    password = password_input.get()

    #checking and giving warning if any field is empty
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title='Missing Entry', message='Fill all the fields to save your password.')
        return 
    
    # asking user yes or no for saving password
    user_response = messagebox.askokcancel(title='Save Prompt', message='Do you want to save your password?')
    if user_response:
        data = get_data()
        # file_data[website.lower()] = {}
        try:
            data[website]
        except KeyError:
            data[website] = {}
        finally:
            data[website][email] = {
            'password': password,
            'added_at' : str(datetime.now())
        }
        save_data(data)
        pyperclip.copy(password)
        reset_fields()
        messagebox.showinfo(title='Success', message='Your password has been saved in the database.')


def search_password():
    website = website_input.get().lower()
    title = 'Search Password'
    if len(website) == 0:
        messagebox.showerror(title, message='You must enter website in order to search in the password database.')
        return
    email = email_input.get().lower()
    if len(email) == 0:
        messagebox.showerror(title, message=f'Enter Email/Username you used to sign up on {website}')
        return

    data = get_data()
    if website in data:
        if email in data[website]:
            password = data[website][email]['password']
            password_input.delete(0, END)
            password_input.insert(0, password)
            pyperclip.copy(password)
            added_at = data[website][email]['added_at']
            messagebox.showinfo(title, message=f'Your {website} account password for {email} is {password} and you saved this on {added_at[:-7]}')
        else:
            messagebox.showerror(title, message=f'No saved {website} account found for {email}')
    else:
        messagebox.showerror(title, message=f'No account saved for {website}')

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.resizable(width=False, height=False)
window.config(padx=20, pady=20)


logo_img = PhotoImage(file='logo.png')
canvas = Canvas(height=200, width=200)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=0, columnspan=3)

#labels
website_label = Label(text='Website:')
website_label.grid(row=1, column=0)

email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0)

password_label = Label(text='Password:')
password_label.grid(row=3, column=0)

#entries

website_input = Entry(width=32)
website_input.grid(row=1, column=1, columnspan=2, sticky=W)
website_input.focus()

search_button = Button(text='Search', command=search_password)
search_button.grid(row=1, column=1, columnspan=2, sticky=E)

email_input = Entry(width=40)
email_input.grid(row=2, column=1, columnspan=2, sticky=W)
email_input.insert(0, 'username@gmail.com')

password_input = Entry(width=21)
password_input.grid(row=3, column=1, columnspan=2, sticky=W)


password_gen_button = Button(text='Generate Password', command=generate_random_password, width=14)
password_gen_button.grid(row=3, column=1, columnspan=2, sticky=E)

# add / save ui
add_button = Button(text='Add', command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky=E+W)

reset_button = Button(text='Reset', command=reset_fields)
reset_button.grid(row=4, column=0, sticky=E+W)


window.mainloop()