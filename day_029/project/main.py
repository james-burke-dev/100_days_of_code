from tkinter import *
from tkinter import messagebox
import random 
from string import ascii_letters, digits
import pyperclip

MY_PASS_PATH = "day_029/project/logo.png"
FONT_NAME = "Courier"
password = ""
password_length = 8
characters = ascii_letters + digits

def generate_password():
    global password
    global password_length
    global characters

    for i in range(1,password_length):
        password += random.choice(characters)
        print(password)
    
    password_textbox.insert(0, password)
    pyperclip.copy(password)

def save_password():
    website = website_textbox.get()
    email = email_textbox.get()
    password = password_textbox.get()

    if len(website) < 1 or len(email) < 1 or len(password) < 1:
        messagebox.askokcancel(title="Oops", message="Please fill out all fields")
    else:
        response = messagebox.askyesno(title=f"{website}", message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it okay to save?")
        if response:
            with open("day_029/project/data.txt", "a") as fn: 
                fn.write(f"{website} | {email} | {password} \n")
            website_textbox.delete(0, END)
            password_textbox.delete(0, END)


window = Tk()
window.title("Password Manager")
#window.minsize(200, 200)
window.config(padx=20, pady=20)

bg_img = PhotoImage( file = MY_PASS_PATH)

bg_canvas = Canvas(width=200, height=200, highlightthickness=0)
bg_canvas.create_image(100, 100, image=bg_img)
bg_canvas.grid(column=1,row=0)

website_label = Label(text="Website:", font=(FONT_NAME, 10))
website_label.grid(column=0, row=1)

website_textbox = Entry()
website_textbox.grid(column=1, row=1, columnspan=2)
website_textbox.focus()


email_label = Label(text="Email/Username:", font=(FONT_NAME, 10))
email_label.grid(column=0, row=2)

email_textbox = Entry()
email_textbox.grid(column=1, row=2, columnspan=2)
email_textbox.insert(0, "test@test.com")

password_label = Label(text="Password:", font=(FONT_NAME, 10))
password_label.grid(column=0, row=3)

password_textbox = Entry()
password_textbox.grid(column=1, row=3)

generate_password_btn = Button(text="Generate Password", command=generate_password)
generate_password_btn.grid(column=3, row=3)

save_btn = Button(text="Save Password", command=save_password)
save_btn.grid(column=1, row=4)

window.mainloop()