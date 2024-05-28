from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
# import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    # pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "email": email,
        "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any empty fields")
    # else:
    #     is_ok = messagebox.askokcancel(title=website,
    #                                    message=f"Details entered; \nEmail: {email} \nPassword: {password}")
    #    if is_ok:
            # with open("data.data", "a") as data_file:
                # From original version
                # data_file.write(f"{website}: {email}  |  {password}\n")
                # website_entry.delete(0, END)
                # password_entry.delete(0, END)
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            # File doesn't exist yet, so create it with "w" and add data
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- SEARCH SAVED INFO ------------------------------- #

def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            # Reading old data
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No logins saved yet.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exist")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels:

website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)

email_label = Label(text="Email / Username: ")
email_label.grid(column=0, row=2)

password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

# Entries:

website_entry = Entry(width=36)
website_entry.grid(column=1, row=1, columnspan=2, sticky="W")
website_entry.focus()
email_entry = Entry(width=46)
email_entry.grid(column=1, row=2, columnspan=2, sticky="W")
email_entry.insert(0, "michalisjk@gmail.com")  # Can also use index END
password_entry = Entry(width=25)
password_entry.grid(column=1, row=3, sticky="W")

# Buttons
gen_pass_button = Button(text="Generate Password", command=generate_password)
gen_pass_button.grid(column=2, row=3, sticky="E")

add_button = Button(text="Add", width=43, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="W")

search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1, sticky="E")

window.mainloop()
