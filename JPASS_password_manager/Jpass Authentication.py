from tkinter import *
from tkinter import messagebox
import os
import sys
import json
from passgen import *
import pyperclip

WHITE = "white"
BLACK = "black"
your_email = ""

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def save_user(username, password):
    user_data = {
        "username": username,
        "password": password
    }
    with open("user.json", "w") as user_file:
        json.dump(user_data, user_file, indent=4)

def authenticate_user(username, password):
    try:
        with open("user.json", "r") as user_file:
            user_data = json.load(user_file)
            return user_data["username"] == username and user_data["password"] == password
    except FileNotFoundError:
        return False

def authentication_screen():
    def login():
        username = username_entry.get()
        password = password_entry.get()
        if authenticate_user(username, password):
            messagebox.showinfo(title="Success", message="Login successful!")
            auth_window.destroy()
            main_app()
        else:
            messagebox.showerror(title="Error", message="Invalid credentials. Please try again.")

    def register():
        username = username_entry.get()
        password = password_entry.get()
        if len(username) == 0 or len(password) == 0:
            messagebox.showerror(title="Error", message="Username and password cannot be empty.")
        else:
            save_user(username, password)
            messagebox.showinfo(title="Success", message="User registered successfully! You can now log in.")

    auth_window = Tk()
    auth_window.title("Authenticate")
    auth_window.config(pady=50, padx=50)

    Label(auth_window, text="Username:").grid(column=0, row=0)
    username_entry = Entry(auth_window, width=35)
    username_entry.grid(column=1, row=0, columnspan=2)

    Label(auth_window, text="Password:").grid(column=0, row=1)
    password_entry = Entry(auth_window, width=35, show="*")
    password_entry.grid(column=1, row=1, columnspan=2)

    login_button = Button(auth_window, text="Login", command=login)
    login_button.grid(column=1, row=2)

    register_button = Button(auth_window, text="Register", command=register)
    register_button.grid(column=2, row=2)

    auth_window.mainloop()

def main_app():
    def insert_password():
        password = generate_password()
        password_entry.delete(0, END)
        password_entry.insert(0, password)
        pyperclip.copy(password)

    def save():
        username = username_entry.get()
        website = website_entry.get()
        password = password_entry.get()
        new_data = {
            website: {
                "email": username,
                "password": password,
            }
        }
        if len(website) == 0 or len(password) == 0:
            messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
        else:
            try:
                with open("data.json", mode="r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", mode="w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", mode="w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

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

    window = Tk()
    window.title("JPass")
    window.config(pady=50, padx=50)

    canvas = Canvas(width=200, height=200)
    mypass_image = PhotoImage(file=resource_path("logo.png"))
    canvas.create_image(100, 100, image=mypass_image)
    canvas.grid(column=1, row=0)

    Label(text="Website:").grid(column=0, row=1)
    website_entry = Entry(width=21)
    website_entry.focus()
    website_entry.grid(column=1, row=1, columnspan=1, sticky=EW)

    Label(text="Email/Username:").grid(column=0, row=2)
    username_entry = Entry(width=35)
    username_entry.insert(0, your_email)
    username_entry.grid(column=1, row=2, columnspan=2, sticky=EW)

    Label(text="Password:").grid(column=0, row=3)
    password_entry = Entry(width=21)
    password_entry.grid(column=1, row=3, sticky=EW)

    Button(text="Generate Password", command=insert_password).grid(column=2, row=3, sticky=EW)
    Button(text="Add", width=36, command=save).grid(column=1, row=4, columnspan=2)
    Button(text="Search", command=find_password).grid(column=2, row=1, sticky=EW)

    window.mainloop()

if __name__ == "__main__":
    authentication_screen()
