"""
Name:       days_hours.py
Purpose:    This program allows the user to input a number in hours and the program will output the number of days and hours

Author:     Mak.L

Created:    08/02/2021
"""

print("****** Hours to Days and Hours ******")

# get number of hours from user
hours = int(input("Enter the number of hours: "))

# compute days and hours
days = hours//24
remaining_hours = hours%24

# output results
print(str(hours) + " hours = " + str(days) + " days and " + str(remaining_hours)+" hours.")


"""
Attempted solution
#User will input number of hours
Hours = float(input("Number of Hours: "))

#Formula to calculate Days
Days = int(Hours / 24)

#Program will output number of days
print("Days: " + str(Days))

#Formula to calculate leftover hours
andHours = (Hours - 24 * Days)

#Program will output leftover hours
print("and Hours: " + str(andHours))
"""