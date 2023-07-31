from tkinter import *

def reset():
    #Clears drop down menus
    inputValue.set(SELECTIONS[0])  
    outputValue.set(SELECTIONS[0])
    
    #Clears text boxes  
    inputBox.delete(0,END)
    outputBox.delete(0,END)
    
    #Sets cursor on inputBox
    inputBox.focus()

def calculate():
    
    
    print("Hi")
    

if __name__ == "__main__": 
    # dictionary of conversion factors  
    unitDict = {  
        "millimeter" : 0.001,  
        "centimeter" : 0.01,  
        "meter" : 1.0,  
        "kilometer" : 1000.0,  
        "foot" : 0.3048,  
        "mile" : 1609.344,  
        "yard" : 0.9144,  
        "inch" : 0.0254,  
        "litre" :  1.0,  
        "millilitre" : 0.001,  
        "gallon" : 3.785,  
        "gram" : 1.0,  
        "kilogram" : 1000.0,  
        "milligram" : 0.001,  
        "ton" : 1000000.0,  
        "pound" : 453.592,  
        "ounce" : 28.3495  
    }  
     
    #list of units
    length_units = [  
        "millimeter", "centimeter", "meter", "kilometer", "foot", "mile", "yard", "inch"  
        ]  
    temperature_units = [  
        "celsius", "fahrenheit"  
    ]  
    volume_units = [  
        "litre", "millilitre", "gallon"     
    ]  
    weight_units = [  
        "gram", "kilogram", "milligram", "ton", "pound", "ounce"  
    ]  
    
    # list of options for selection menu  
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

    calculatorLabel = Label(root, text="UNIT CONVERSION CALCULATOR", font = ("roboto", 19) )
    calculatorLabel.pack(pady = 30)

    #Input Area
    inputFrame = Frame(root)
    inputFrame.pack(ipadx= 40)

    inputLabel = Label(inputFrame, text="From:", bg="#6E6E6E", fg = "#ffffff", font = 12)
    inputLabel.pack(side='left', pady= 30)

    # Option menu  
    inputMenu = OptionMenu(inputFrame,  inputValue, *SELECTIONS  )  
    inputMenu.pack(side="right")
    
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
            
    calculateButton = Button(root, text = "CALCULATE", command = calculate, fg="#ffffff", bg="#5e5e5e")
    calculateButton.pack()
    
    resetButton = Button(root, text = "RESET", command = reset, bg= "red")
    resetButton.pack()

    root.mainloop() 