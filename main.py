from tkinter import *
from tkinter import messagebox
import pyperclip

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Go to: https://replit.com/@appbrewery/password-generator-start?v=1
import random
def generatePass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    nr_letters= random.randint(8,10)
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)

    passLen = nr_letters + nr_numbers + nr_symbols

    letterList = random.sample(letters,nr_letters)

    numberList = random.sample(numbers,nr_symbols)

    symbolList = random.sample(symbols,nr_numbers)


    selected_LNS=(letterList+numberList+symbolList)

    finalPassword=random.sample(selected_LNS,passLen)
    finalPassword=''.join(finalPassword)

    password_DataField.delete(0,END)
    password_DataField.insert(0,finalPassword)
    pyperclip.copy(finalPassword)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def savePassword():
    website=website_DataField.get()
    email=email_DataField.get()
    password=password_DataField.get()

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Oops",message="Please don't any fields empty!")

    else:

        isOk = messagebox.askokcancel(title=website,message=f"This're the details entred: \nEmail: {email}\nPassoord: "
                                                         f"{password}\n\nHit OK for save!")
        if isOk:
            with open('data.txt', 'a') as file:
                file.write(f"{website} | {email} | {password}\n")
                website_DataField.delete(0, END)
                password_DataField.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
canvas=Canvas(width=200,height=200)

lock=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock)
canvas.grid(column=1,row=0)

website_LBL=Label(text="Website: ")
website_LBL.grid(column=0,row=1)

website_DataField=Entry(width=60)
website_DataField.focus()
website_DataField.grid(column=1,row=1,columnspan=2)#,columnspan=2

email_LBL= Label(text="Email/UserName: ")
email_LBL.config(pady=5)
email_LBL.grid(column=0,row=2)

email_DataField= Entry(width=60)
email_DataField.insert(0,"mamun@gmail.com")
email_DataField.grid(column=1,row=2,columnspan=2)


password_LBL=Label(text="Password: ")
password_LBL.config(pady=5)
password_LBL.grid(column=0,row=3)


password_DataField=Entry(width=35)
password_DataField.grid(column=1,row=3)


passwordGenerate_Btn=Button(text="Generate Password",width=19,command=generatePass)
passwordGenerate_Btn.grid(column=2,row=3)



add_btn=Button(text="Add",width=40,command=savePassword)
add_btn.grid(column=1,row=4,columnspan=2)


window.mainloop()