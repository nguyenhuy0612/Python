import tkinter as ob

def Set_Message():
    text = text_input.get()
    title_label.configure(text=text)



windows = ob.Tk()
windows.title("Tkinter")
windows.minsize(width=500,height=500)

title_label = ob.Label(master=windows,text="User")
title_label.pack()

text_input = ob.Entry(master=windows)
text_input.pack()

Submit_button = ob.Button(master=windows,text="Submit",command=Set_Message)
Submit_button.pack()

windows.mainloop()