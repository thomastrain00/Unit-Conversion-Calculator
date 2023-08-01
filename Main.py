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
    #Getting variables from user
    valueToConvert = float(inputBox.get())
    inputUnit = inputValue.get()
    outputUnit = outputValue.get()
    
    # list of the required combination of the conversion factors  
    conversionFactors = [inputUnit in lengthUnits and outputUnit in lengthUnits,  
    inputUnit in weightUnits and outputUnit in weightUnits,  
    inputUnit in temperatureUnits and outputUnit in temperatureUnits,  
    inputUnit in volumeUnits and outputUnit in volumeUnits]  
    
    if any(conversionFactors): # If both the units are of same type, perform the conversion  
            if inputUnit == "celsius" and outputUnit == "fahrenheit":  
                outputBox.delete(0, END)  
                outputBox.insert(0, (valueToConvert * 1.8) + 32)  
                # Temperature conversions use different method to convert
            elif inputUnit == "fahrenheit" and outputUnit == "celsius":  
                outputBox.delete(0, END)  
                outputBox.insert(0, (valueToConvert - 32) * (5/9))  
            else:  
                outputBox.delete(0, END)  
                outputBox.insert(0, round(valueToConvert * unitDict[inputUnit] / unitDict[outputUnit], 5))  
    
    else:  
        # displaying error if units are of different types  
        outputBox.delete(0, END)  
        outputBox.insert(0, "ERROR, invalid type")      

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
    lengthUnits = [  
        "millimeter", "centimeter", "meter", "kilometer", "foot", "mile", "yard", "inch"  
        ]  
    temperatureUnits = [  
        "celsius", "fahrenheit"  
    ]  
    volumeUnits = [  
        "litre", "millilitre", "gallon"     
    ]  
    weightUnits = [  
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
        "gallon",     
        "gram",  
        "kilogram",  
        "milligram",  
        "pound",  
        "ounce"  
    ]  

    root = Tk() #create a root widget/ main window
    root.title("Unit Conversion Calculator")
    root.resizable(0,0) #makes it unresizable
    root.geometry("500x450+600+250")  # (width x height) + x + y axis, default position on the screen on startup
    
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