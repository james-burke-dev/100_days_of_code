import tkinter

window = tkinter.Tk()
window.title("Miles to KMs Converter")
window.minsize(100,150)
window.config(padx=25, pady=50)

def convert():
    user_data = float(text_input.get())
    kms = user_data * 1.609
    ans_label.config(text=f"{kms}")
    

equal_to_label = tkinter.Label(text="is equal to")
equal_to_label.grid(column=0, row=1)

ans_label = tkinter.Label(text="0")
ans_label.grid(column=1,row=1)

kms_label = tkinter.Label(text="Km")
kms_label.grid(column=2,row=1)

text_input = tkinter.Entry(width=10)
text_input.grid(column=1,row=0)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2,row=0)

button = tkinter.Button(text="Convert!", command=convert)
button.grid(column=1,row=2)

window.mainloop()