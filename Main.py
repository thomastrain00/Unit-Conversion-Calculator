#convert freedom units to metric
#use a library to have a ui (tkinter?)
#use swtich cases to adjust for input?

from tkinter import *
frame = Tk() #create a root widget/ main window

frame.title("Unit Conversion Calculator")
#frame.configure(background="RED")
frame.minsize(500, 200)  # width, height
frame.maxsize(500, 500)
frame.geometry("500x300")  # (width x height) + x + y axis, default position on the screen on startup

#Creating Text Input Box
inputText = Text(frame, height = 1, width=20)

inputText.pack() #.pack() puts it on the window

frame.mainloop() # needed to render the gui