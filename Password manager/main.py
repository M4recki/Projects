import customtkinter as ctk
from PIL import Image
from tkinter import END
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def PasswordGenerator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for i in range(randint(8, 10))]
    password_numbers = [choice(numbers) for i in range(randint(2, 4))]
    password_symbols = [choice(symbols) for i in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    secret_password = "".join(password_list)
    password_entry.insert(0, secret_password)
    pyperclip.copy(secret_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def Error(error_message):
    pop_up_1 = ctk.CTkToplevel()
    pop_up_1.geometry("300x300")
    pop_up_1.title("Error")

    # Label
    error_description_1 = ctk.CTkLabel(
        master=pop_up_1, text=error_message, font=font)
    error_description_1.grid(row=0, column=0, padx=10, pady=20)

    # Confirmation button
    confirmation_button_1 = ctk.CTkButton(
        master=pop_up_1, width=50, text="OK", corner_radius=5, command=lambda: Quit(pop_up=pop_up_1), fg_color="red", hover_color="dark red")
    confirmation_button_1.grid(row=1, column=0, pady=50, padx=125)


def Success(success_message):
    pop_up_2 = ctk.CTkToplevel()
    pop_up_2.geometry("300x300")
    pop_up_2.title("Email/Username & Password")

    # Label
    description = ctk.CTkLabel(
        master=pop_up_2, text=success_message, font=font)
    description.grid(row=0, column=0, padx=10, pady=20)

    # Confirmation button
    confirmation_button_2 = ctk.CTkButton(
        master=pop_up_2, width=50, text="OK", corner_radius=5, command=lambda: Quit(pop_up=pop_up_2), fg_color="red", hover_color="dark red")
    confirmation_button_2.grid(row=1, column=0, padx=125, pady=50)


def SearchPassword():

    # User details
    Email = email_entry.get()
    Password = password_entry.get()
    Website = website_entry.get()

    # Load data
    try:
        with open("passwords.json", "r") as data_file:
            data = json.load(data_file)

            email = data[Email]["email"]
            user_password = data[Password]["password"]

        Success(
            success_message=f"Email: \n{email}\n password: \n{user_password}")

    except (KeyError, json.decoder.JSONDecodeError):
        Error(
            error_message=f"Website: \n'{Website}'\n does not exist. Make sure you entered website's\n name correctly or create new website's details.")


def Add():

    # User details
    Email = email_entry.get()
    Password = password_entry.get()
    Website = website_entry.get()

    # JSON
    new_data = {website_entry.get():
                {
        "email": Email,
        "password": Password
    }
    }

    # Empty fields
    if len(Website) == 0 or len(Password) == 0:

        Error(error_message="Please make sure you haven't left any fields empty.")

    # Invalid email or website link
    elif "@" not in email_entry.get():

        Error(error_message="Please make sure you incuded '@' in your email.")

    # Everything OK (load, update or create data)
    else:
        try:
            with open("passwords.json", "r") as file:

                data = json.load(file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            with open("passwords.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)

            with open("passwords.json", "w") as file:
                json.dump(data, file, indent=4)

        finally:
            Success(
                success_message=f"Your website:\n '{Website}'\n and password: \n'{Password}'\n were successfully added to file 'passwords.json'")

            website_entry.delete(0, END)
            password_entry.delete(0, END)


def Quit(pop_up):
    pop_up.destroy()
    pop_up.update()


def change_appearance_mode_event(new_appearance_mode: str):
    ctk.set_appearance_mode(new_appearance_mode)


def change_scaling_event(new_scaling: str):
    new_scaling_float = int(new_scaling.replace("%", "")) / 100
    ctk.set_widget_scaling(new_scaling_float)


# ---------------------------- UI SETUP ------------------------------- #
ctk.set_appearance_mode("System")
App = ctk.CTk()
App.geometry("700x600")
App.title("MyPass by Marek Baranski")


font = ("Noto Sans", 12)

# Appearance mode
appearance_mode_label = ctk.CTkLabel(
    master=App, text="Appearance Mode:", text_color="red", font=font)
appearance_mode_label.grid(row=0, column=0, pady=10)

appearance_mode_optionmenu = ctk.CTkOptionMenu(
    master=App, values=["System", "Dark", "Light"], fg_color="red",  button_color="red", button_hover_color="dark red",  dropdown_hover_color="dark red", command=change_appearance_mode_event)
appearance_mode_optionmenu.grid(row=1, column=0, padx=30)

# Scaling
scaling_label = ctk.CTkLabel(
    master=App, text="UI Scaling:", text_color="red", font=font)
scaling_label.grid(row=0, column=2, pady=10)

scaling_optionmenu = ctk.CTkOptionMenu(master=App, values=[
    "80%", "90%", "100%", "110%", "120%"], fg_color="red",  button_color="red", button_hover_color="dark red",  dropdown_hover_color="dark red", command=change_scaling_event)
scaling_optionmenu.set("100%")
scaling_optionmenu.grid(row=1, column=2, padx=30)

# Logo
img = ctk.CTkImage(Image.open("logo.png"), size=(200, 200))

img_display = ctk.CTkLabel(master=App, image=img, text="", padx=20, pady=20)
img_display.grid(row=2, column=1, padx=1, pady=50)

# Website
website = ctk.CTkLabel(master=App, text="Website:",
                       font=font, text_color="red")
website.grid(row=3, column=0)

website_entry = ctk.CTkEntry(
    master=App, width=300, placeholder_text="Type here your website name", placeholder_text_color="red")
website_entry.grid(row=3, column=1)
website_entry.focus()

# Search button
search_button = ctk.CTkButton(
    master=App, width=150, text="Search", corner_radius=5, fg_color="red", hover_color="dark red", command=SearchPassword)
search_button.grid(row=3, column=2)

# Email
email = ctk.CTkLabel(master=App, text="Email:",
                     font=font, text_color="red")
email.grid(row=4, column=0, pady=10)

email_entry = ctk.CTkEntry(
    master=App, width=300, placeholder_text="Type here your email address or username", placeholder_text_color="red")
email_entry.grid(row=4, column=1, pady=10)
email_entry.insert(0, "marekbaranski0@gmail.com")

# Password
password = ctk.CTkLabel(master=App, text="Password:",
                        font=font, text_color="red")
password.grid(row=5, column=0)

password_entry = ctk.CTkEntry(
    master=App, width=300, placeholder_text="Type here your password", placeholder_text_color="red")
password_entry.grid(row=5, column=1)

# Generate random password
generate_random_password = ctk.CTkButton(
    master=App, width=150, text="Generate password", corner_radius=5, fg_color="red", hover_color="dark red", command=PasswordGenerator)
generate_random_password.grid(row=5, column=2)

# Add everything
add = ctk.CTkButton(
    master=App, width=300, text="Add", corner_radius=5, command=Add, fg_color="red", hover_color="dark red")
add.grid(row=6, column=1, pady=10)

App.mainloop()
