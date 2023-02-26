import json
from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
import pyperclip

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

import random


def generatePass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    passLen = nr_letters + nr_numbers + nr_symbols

    letterList = random.sample(letters, nr_letters)

    numberList = random.sample(numbers, nr_symbols)

    symbolList = random.sample(symbols, nr_numbers)

    selected_LNS = (letterList + numberList + symbolList)

    finalPassword = random.sample(selected_LNS, passLen)
    finalPassword = ''.join(finalPassword)

    password_DataField.delete(0, END)
    password_DataField.insert(0, finalPassword)
    pyperclip.copy(finalPassword)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def savePassword():
    website = website_DataField.get().title()
    email = email_DataField.get()
    password = password_DataField.get()

    newData = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't any fields empty!")

    else:

        # isOk = messagebox.askokcancel(title=website,message=f"This're the details entred: \nEmail: {email}\nPassoord: "
        #                                               f"{password}\n\nHit OK for save!")
        try:
            with open('data.json', 'r') as file:
                loadData = json.load(file)

        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(newData, file, indent=4)

        except JSONDecodeError:
            """This error occared When the json file have Empty"""
            with open("data.json", "w") as file:
                json.dump(newData, file, indent=4)

        else:
            loadData.update(newData)
            with open("data.json", "w") as file:
                json.dump(loadData, file, indent=4)

        finally:
            website_DataField.delete(0, END)
            password_DataField.delete(0, END)


# ---------------------------- Search ------------------------------- #
def search():
    website=website_DataField.get().title()
    try:
        with open("data.json","r") as file:
            loadData=json.load(file)
            email=loadData[website].get("email")
            passwrd = loadData[website].get("password")
            messagebox.showinfo(title="User Details", message=f"Email: {email}\nPassoord: {passwrd}")

    except KeyError:
        messagebox.showerror(title="Error", message="No Details for the website exists!")
    except:
        messagebox.showerror(title="Error",message="No Data Found!")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)

lock = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock)
canvas.grid(column=1, row=0)

website_LBL = Label(text="Website: ")
website_LBL.grid(column=0, row=1)

website_DataField = Entry(width=38)
website_DataField.focus()
website_DataField.grid(column=1, row=1)  # ,columnspan=2

email_LBL = Label(text="Email/UserName: ")
email_LBL.config(pady=5)
email_LBL.grid(column=0, row=2 )

email_DataField = Entry(width=70)
email_DataField.insert(0, "mamun@gmail.com")
email_DataField.grid(column=1, row=2, columnspan=2)

password_LBL = Label(text="Password: ")
password_LBL.config(pady=5)
password_LBL.grid(column=0, row=3)

password_DataField = Entry(width=38)
password_DataField.grid(column=1, row=3)

passwordGenerate_Btn = Button(text="Generate Password", width=25, command=generatePass)
passwordGenerate_Btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=60, command=savePassword)
add_btn.grid(column=1, row=4, columnspan=2)

search_Btn=Button(text="Search", width=25,command=search)
search_Btn.grid(column=2,row=1)


window.mainloop()
