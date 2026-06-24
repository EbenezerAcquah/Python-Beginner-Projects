#Temperature Converter

#Conversion Functions
def Celsius_to_Fahrenheit(temperature):
    return (temperature * 9/5) + 32

def Fahrenheit_to_Celsius(temperature):
    return (temperature - 32) * 5/9

def Celsius_to_Kelvin(temperature):
    return temperature + 273.15

def Kelvin_to_Celsius(temperature):
    return temperature - 273.15

def Fahrenheit_to_Kelvin(temperature):
    return (temperature - 32) * 5/9 + 273.15

def Kelvin_to_Fahrenheit(temperature):
    return (temperature - 273.15) * 9/5 + 32

#Display menu to user
print("==== TEMPERATURE CONVERTER ====")
print("1. Change temperature from Celsius to Fahrenheit")
print("2. Change temperature from Fahrenheit to Celsius")
print("3. Change temperature from Celsius to Kelvin")
print("4. Change temperature from Kelvin to Celsius")
print("5. Change temperature from Fahrenheit to Kelvin")
print("6. Change temperature from Kelvin to Fahrenheit")


try: 
    choice = int(input("Select an option: "))

    #Float allows decimal numbers such as 99.9
    temperature = float(input("Enter the temperature: "))
        
    if choice == 1:
        results = Celsius_to_Fahrenheit(temperature)
        print(f"{results}°F")
            
    elif choice == 2:
        results = Fahrenheit_to_Celsius(temperature)
        print(f"{results}°C")
        
    elif choice == 3:
        results = Celsius_to_Kelvin(temperature)
        print(f"{results}K")
            
    elif choice == 4:
        results = Kelvin_to_Celsius(temperature)
        print(f"{results}°C")
            
    elif choice == 5:
        results = Fahrenheit_to_Kelvin(temperature)
        print(f"{results}K")
    
    elif choice == 6:
        results = Kelvin_to_Fahrenheit(temperature)
        print(f"{results}°F")
            
    #Runs if user enters a number outside 1 - 6
    else:
        print("Invalid Input")

#Runs if int() or float() cannot convert user's input
except ValueError:
    print("Please enter a valid number.")

# "f" introduced here in the print command tells Python to look inside the curly braces{}
# and replace them with the actual values.