from tkinter import *
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height = 300)
window.config(padx=100,pady = 20)

entry = Entry()
entry.get()
entry.grid(column=2, row = 0)

text = Label(text="Miles")
text.grid(column=3, row = 0)

text2 = Label(text="is equal to :")
text2.grid(column=1,row=2)

conversion = Label(text="0")
conversion.grid(column=2,row=2)

text3 = Label(text="km")
text3.grid(column=3,row=2)

def button_clicked():
    string_input = entry.get()
    integer_input = int(string_input)
    converted_value = integer_input*1.6
    conversion["text"] = converted_value

button = Button(text= "Convert",command=button_clicked)
button.grid(column=2,row = 3)


window.mainloop()