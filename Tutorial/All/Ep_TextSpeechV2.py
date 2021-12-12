
#? Import Libraries
import win32com.client
import tkinter as ui
#? Import Libraries

speaker = win32com.client.Dispatch("SAPI.SpVoice")

#!---------------------------------------------------------------------------------------
#? Funtion
def Set_Message():
    text = text_input.get()
    title_label.configure(text=text)
    speaker.Speak(text)
#!---------------------------------------------------------------------------------------    


#!---------------------------------------------------------------------------------------
#? Program 

#? UI Program
windows = ui.Tk()

#? Text 
windows.title("Text Speech",)
#? Text

#? Width And Height
windows.minsize(width=300,height=200)
#? Width And Height

#? Label
title_label = ui.Label(master=windows,text="Program Text Speech")
title_label.pack(pady=25)
#? Label

#? Input
text_input = ui.Entry(master=windows)
text_input.pack()
#? Input

#? Button
Submit_button = ui.Button(master=windows,text="Speech!!!",command=Set_Message,width=15,height=2)
Submit_button.pack()
#? Button

#? Loop Program
windows.mainloop()
#? Loop Program

#!---------------------------------------------------------------------------------------