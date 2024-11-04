from tkinter import *
from tkinter import messagebox
import os
import sys
from passgen import *
import pyperclip
import json
WHITE = "white"
BLACK = "black"
your_email = ""
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def insert_password():
    password = generate_password()
    password_entry.delete(0, END)
    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    username = username_entry.get()
    website = website_entry.get()
    password = password_entry.get()
    new_data = {
        website:    {
            "email": username,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please dont leave any fields empty")
    else:
        try:
            with open(file="data.json", mode="r") as data_file:
                #reading old data
                data = json.load(data_file)
                #updating old data with new data

        except FileNotFoundError:
            with open(file="data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)

        except json.JSONDecodeError:
            print(
                "data is corrupted or this is the first time you are trying to add a password \n creating new database...")
            with open(file="data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
            #wrting updated data to json file

        else:
            data.update(new_data)
            with open(file="data.json",mode = "w") as data_file:
                json.dump(data, data_file, indent=4)


        finally:
            # clearing entry fields for website and password
            website_entry.delete(first=0, last=END)
            password_entry.delete(first=0, last=END)

#-----------------------------File handling-------------------------------#

def resource_path(relative_path):
    "gets the absolute path of a resource, maybe best to handle this in a better way in the future"
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


mypass_image = resource_path("logo.png")
# ---------------------------- Search handling ------------------------------- #
def find_password():
    search = website_entry.get().lower()
    try:
        with open("data.json", mode="r") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data Found")
    else:
        matches = [key for key in data if key.lower().startswith(search)]
        if matches:
            found_entry = data[matches[0]]
            found_email = found_entry["email"]
            found_password = found_entry["password"]
            messagebox.showinfo(title="Info", message=f"Username:{found_email} Password:{found_password}")
        else:
            messagebox.showinfo(title="Error", message=f"The website: {search}, was not found in the database")




# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("JPass")
window.config(pady=50, padx=50)


canvas  = Canvas(width=200, height=200)
mypass_image = PhotoImage(file=mypass_image,)
canvas.create_image(100,100, image=mypass_image,)
canvas.grid(column=1, row=0)

#-------- website -----#
website_label = Label(text="Website:")
website_label.grid(column= 0,row= 1)
website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(column= 1 ,row= 1, columnspan=1, sticky=EW)
#-------- email/username -----#
username_label = Label(text="Email/Username:")
username_label.grid(column= 0,row= 2)
username_entry = Entry(width=35)
username_entry.insert(0, f"{your_email}")
username_entry.grid(column= 1 ,row= 2, columnspan=2,sticky=EW)
#-------- password -----#
password_label = Label(text="Password:")
password_label.grid(column= 0,row= 3)
password_entry = Entry(width=21)
password_entry.grid(column= 1,row= 3,sticky=EW)
password_button = Button(text="Generate Password", command=insert_password)
password_button.grid(column= 2, row=3, sticky=EW)
#-------- add -----#
add_button = Button(text="Add", width= 36, command=save)
add_button.grid(column = 1 , row= 4, columnspan=2)
#-------- Search -----#
search_button = Button(text="Search", command= find_password)
search_button.grid(column = 2, row= 1, sticky = EW)

#SQLLITE for database structure LOOK INTO IT


mainloop()