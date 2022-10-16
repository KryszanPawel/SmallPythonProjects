from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

YOUR_EMAIL = "youremail@provide.com"

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- Find in Json------------------------------- #
def find():
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
            searching = web_entry.get()
    except FileNotFoundError:
        messagebox.showinfo(title=f"File not found",
                            message="There is no password in database")
    else:
        if searching in data:
            messagebox.showinfo(title=f"Your login data to {searching}",message=f"Username: {data[searching]['email']}\nPassword: {data[searching]['password']}")
        else:
            messagebox.showinfo(title=f"Data not found for {searching}",
                                message=f"There is no login data to this website")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    password_entry.delete(0, END)
    password_entry.insert(0, "")

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def adding():
    website = web_entry.get()
    email = username_entry.get()
    password = password_entry.get()
    new_data = {
        website : {
            'email' : email,
            'password' : password
        }
    }

    if len(email) == 0 or len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title= website,message=f"These are the details entered: \n Email: {email}\n "
                                                      f"Password: {password}\n Is that ok to save?")

        if is_ok:
            try:
                with open("data.json", mode="r") as data_file:
                    data = json.load(data_file)
                    data.update(new_data)
            except FileNotFoundError:
                data = new_data
            finally:
                with open("data.json", mode="w") as data_file:
                    json.dump(data,data_file,indent=4)
                web_entry.delete(0, END)
                web_entry.insert(0, "")
                password_entry.delete(0, END)
                password_entry.insert(0, "")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
window.minsize(200, 200)

canvas = Canvas(width=200, height=200)
myimg = PhotoImage(file='logo.png')
canvas.create_image(80, 100, image=myimg)
canvas.grid(column=1, row=0, sticky="w")

# Website label
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

# Website inbox
web_entry = Entry(width=21)
web_entry.grid(column=1, columnspan=2, row=1, sticky="w")
web_entry.focus()

# Username label
username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

# Username inbox
username_entry = Entry(width=40)
username_entry.grid(column=1, columnspan=2, row=2, sticky="w")
username_entry.insert(END, YOUR_EMAIL)

# Password label
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Password inbox
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="w")

# Generate button
generate = Button(width=15, text="Generate Password", command=generate)
generate.grid(column=1, columnspan=2, row=3, sticky="e")

# Add button
add = Button(width=34, text="Add", command=adding)
add.grid(column=1, row=4, columnspan=2, sticky="w")

# Search button
search = Button (width=15, text="Search", command=find)
search.grid(column=1,columnspan=2,row=1,sticky="e")

window.mainloop()

