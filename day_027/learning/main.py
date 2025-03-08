import tkinter

window = tkinter.Tk()
window.title("Gui Program")
window.minsize(500,300)

temp_label = tkinter.Label(text="Label label", font=("Arial", 24))
# temp_label.pack()
temp_label.grid(column=0,row=0)

def button_click():
    user_data = text_input.get()
    temp_label.config(text=user_data)
    print("Click received")

button = tkinter.Button(text="Click me!", command=button_click)
button.grid(column=1,row=1)

text_input = tkinter.Entry(width=10)
text_input.grid(column=3,row=2)
#temp_label.grid(column=1,row=2)

new_button = tkinter.Button(text="Convert!", command=button_click)
new_button.grid(column=2,row=0)

window.mainloop()
