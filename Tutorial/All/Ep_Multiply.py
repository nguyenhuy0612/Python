
import tkinter as tk
from tkinter.constants import W

#!------------------------------------------------------------------------------------
#! Funtion
def show_output():

    number = int(number_input.get())

    if number == 0:
        output_label.configure(text="Error")
        return

    output = ""

    for i in range(1,13):
        output += str(number) + " x " + str(i)
        output += " = " + str(number * i) + "\n"

    output_label.configure(text=output)

#!---------------------------------------------------------------------------------------
    #? Program
Prpgram = tk.Tk()
Prpgram.title("Multiply")
Prpgram.minsize(width=270, height=390)

title_label = tk.Label(master=Prpgram, text="สูตรคูณแม่")
title_label.pack(pady=20)

number_input = tk.Entry(master=Prpgram,width=15)
number_input.pack()

Submit_button = tk.Button(
    master=Prpgram, text="Submit",
    command=show_output,width=15,height=2
    )
Submit_button.pack()

output_label = tk.Label(master=Prpgram)
output_label.pack(pady=20)

Prpgram.mainloop()
#!---------------------------------------------------------------------------------------