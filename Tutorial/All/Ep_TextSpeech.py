
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

while 1 :
    s = input("Text Speaker:")
    speaker.Speak(s)
     
# End of file