import tkinter as tk 
from gtts import gTTS #pip install gtts
from playsound import playsound #pip install playsound

win=tk.Tk() 
win.title("Text To Speech") 
win.geometry("200x70") 

#function to convert Text to Speech using gTTS 
#The speech is saved and is played using playsound
def text_to_speech():
    text=entry.get()
    speech=gTTS(text=text,lang="en")
    speech.save(r'<Location you want To save your Mp3 file>') 
    #For eg: speech.save(r'C:\Users\username\Downloads\speech.mp3')
    playsound(r'<Location you saved your Mp3 file>')  
    #For eg: playsound(r'C:\Users\username\Downloads\speech.mp3')


label=tk.Label(win,text="Enter Text Here :") 
label.grid(row=0,column=0) 

#To get the text entry from user 
entry=tk.Entry(win) 
entry.grid(row=1,column=0) 

#Button to convert Text to Speech
#Clicking on this button will call text_to_speech function
button=tk.Button(win,text="Go",command=text_to_speech) 
button.grid(row=1,column=1)

win.mainloop()