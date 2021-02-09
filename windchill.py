"""
Name:       windchill.py
Purpose:    This program allows the user to input a the degree in celsius and windspeed to calculate the 

Author:     Mak.L

Created:    08/02/2021
"""

print ("******Windchill******")
print("")

#User will input temperature and wind speed
temp_c = float(input("Enter the temperature in celsius: "))
windspeed = float(input("Enter the wind speed in km/h: "))

#formula for windchill
windchill = 13.12 + (0.6215 * temp_c) - (11.37 * windspeed ** 0.16) + (0.3965 * temp_c * windspeed ** 0.16)

# output windchill
print("With the windchill factor, it feels like " + str(windchill) + "° outside.")
print("With the windchill factor, it feels like " + str(round(windchill,1)) + "° outside.")