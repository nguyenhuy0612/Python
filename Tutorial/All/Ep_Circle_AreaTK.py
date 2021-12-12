
import tkinter as tk
from tkinter.constants import W

#!------------------------------------------------------------------------------------
#! Funtion
def Get_Circle_Area():

    number = int(number_input.get())

    radius = 22/7 * (number**2)    

    output_label.configure(text=radius)
       

#!---------------------------------------------------------------------------------------
    #? Program
Prpgram = tk.Tk()
Prpgram.title("Area")
Prpgram.minsize(width=270, height=390)

title_label = tk.Label(master=Prpgram, text="พื้นที่วงกลม")
title_label.pack(pady=5)

number_input = tk.Entry(master=Prpgram,width=15)
number_input.pack()

Submit_button = tk.Button(
    master=Prpgram, text="Submit",
    command=Get_Circle_Area,width=15,height=2
    )

Submit_button.pack(pady=10)

output_label = tk.Label(master=Prpgram)
output_label.pack(pady=20)

Prpgram.mainloop()
#!---------------------------------------------------------------------------------------