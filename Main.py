from tkinter import *

def calculate():
    print("Hi")
    
def reset():
    print("Woah")


if __name__ == "__main__":  
    # creating the list of options for selection menu  
    SELECTIONS = [  
        "Select Unit",  
        "millimeter",  
        "centimeter",  
        "meter",  
        "kilometer",  
        "foot",  
        "mile",  
        "yard",  
        "inch",  
        "celsius",  
        "fahrenheit", 
        "litre",  
        "millilitre",  
        "gallon"     
        "gram",  
        "kilogram",  
        "milligram",  
        "pound",  
        "ounce"  
    ]  

    root = Tk() #create a root widget/ main window
    

    root.title("Unit Conversion Calculator")
    root.resizable(0,0) #makes it unresizable
    root.geometry("500x450")  # (width x height) + x + y axis, default position on the screen on startup
    
    #Setting Default Values
    inputValue = StringVar()
    outputValue = StringVar()
    inputValue.set(SELECTIONS[0])  
    outputValue.set(SELECTIONS[0])  

    calculatorLabel = Label(root, text="UNIT CONVERSION CALCULATOR", font = ("arial black", 19), fg = "#6E6E6E" )
    calculatorLabel.pack(pady = 30)

    #Input Area
    inputFrame = Frame(root)
    inputFrame.pack(ipadx= 40)

    inputLabel = Label(inputFrame, text="From:", bg="#6E6E6E", fg = "#ffffff", font = 12)
    inputLabel.pack(side='left', pady= 30)

    # adding the option menus to the main window  
    input_menu = OptionMenu(inputFrame,  inputValue, *SELECTIONS  )  
    input_menu.pack(side="right")
    
    inputBox = Entry(inputFrame, bd=3)
    inputBox.pack(side='right')


    
    #Output Area
    outputFrame = Frame(root)
    outputFrame.pack(ipadx= 50)

    outputLabel = Label(outputFrame, text="To:", bg="#6E6E6E", fg = "#ffffff", font = 12)
    outputLabel.pack(side='left', pady= 30)

    # adding the option menus to the main window  
    outputMenu = OptionMenu(outputFrame, outputValue, *SELECTIONS  )  
    outputMenu.pack(side="right")
    
    outputBox = Entry(outputFrame, bd=3)
    outputBox.pack(side='right')
            
    calculateButton = Button(root, text = "CALCULATE", command = calculate)
    calculateButton.pack()
    
    resetButton = Button(root, text = "RESET", command = reset, bg= "red")
    resetButton.pack()

    root.mainloop() 