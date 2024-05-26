from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #



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

website_entry = Entry(width=46)
website_entry.grid(column=1, row=1, columnspan=2, sticky="W")
website_entry.focus()
email_entry = Entry(width=46)
email_entry.grid(column=1, row=2, columnspan=2, sticky="W")
email_entry.insert(0, "michalisjk@gmail.com")  # Can also use index END
password_entry = Entry(width=25)
password_entry.grid(column=1, row=3, sticky="W")

# Buttons
gen_pass_button = Button(text="Generate Password")
gen_pass_button.grid(column=2, row=3, sticky="E")
add_button = Button(text="Add", width=43)
add_button.grid(column=1, row=4, columnspan=2, sticky="W")

window.mainloop()
