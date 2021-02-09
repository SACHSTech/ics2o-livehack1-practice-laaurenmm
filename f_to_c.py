"""
Name:       f_to_c.py
Purpose:    This program allows the user to input a degree in Fahrenheit and the program will print out the degree in Celsius

Author:     Mak.L

Created:    08/02/2021
"""
#User will input Degree in Fahrenheit
DegreeF = float(input("Degree in Fahrenheit: "))
print ("")

#Formula to convert Degree in Fahrenheit to Celsius 
DegreeC = str((DegreeF - 32) * 5/9)

#Program will output degree in Celcius 
print("Degree in Celsius: " + (DegreeC))


"""
other solution
temp_f = float(input("Enter the temperature in Fahrenheit: "))

# compute celsius
temp_c = (5/9) * (temp_f - 32)  
temp_c = (5/9) * (temp_f-32)  

# output celsius
print("The temperature in Celsius is " + str(temp_c) + "°.")
"""