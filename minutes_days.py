"""
Name:       minutes_days.py
Purpose:    This program allows the user to input a number in minutes and the program will output the number of days, hours and minutes

Author:     Mak.L

Created:    09/02/2021
"""
print("****** Minutes to Days and Hours ******")

# get number of minutes from user
minutes = int(input("Enter the number of minutes: "))

# compute days and hours
days = minutes//1440
remaining_minutes = minutes%1440
hours = remaining_minutes//60
final_minutes = remaining_minutes - hours*60

# output results
print(str(minutes) + " minutes is " + str(days) + " day(s) " + str(hours)+" hour(s) and " + str(final_minutes) + " minute(s)."

"""