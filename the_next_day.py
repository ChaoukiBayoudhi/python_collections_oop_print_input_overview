
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
months = {1: ('January', 31), 2: ('February', 28), 3: ('March', 31), 4: ('April', 30),
          5: ('May', 31), 6: ('June', 30), 7: ('July', 31), 8: ('August', 31),
          9: ('September', 30), 10: ('October', 31), 11: ('November', 30), 12: ('December', 31)}

def next_day(date):
    # Calculate the next day of the week
    next_day_name = days[(days.index(date[0]) + 1) % 7]
    next_year = date[3]  # Initialize next year as the current year
    
    # Check if the current date is December 31st and update accordingly
    if date[2] == 12 and date[1] == 31:
        next_month = 1  # Move to January
        next_year = date[3] + 1  # Increment the year
        next_day_of_month = 1  # Reset the day of the month to 1
    # Check for specific month and day combinations that require a month change
    elif date[2] == 2 and date[1] == 28 and date[3] % 4 == 0 and (date[3] % 100 != 0 or date[3] % 400 == 0) or (date[2] in (4, 6, 9, 11) and date[1] == 30) or (date[2] in (1, 3, 5, 7, 8, 10) and date[1] == 31) or (date[2] == 2 and date[1] == 29):
        next_month = date[2] + 1  # Move to the next month
        next_day_of_month = 1  # Reset the day of the month to 1
    else:
        next_month = date[2]  # Keep the current month
        next_day_of_month = date[1] + 1  # Increment the day of the month
    
    return (next_day_name, next_day_of_month, next_month, next_year) 
#test
#feb 29 2000 (year leap)
print(next_day(("Monday",28,2,2000))) # should print ('Tuesday', 29, 2, 2000)
#feb 28 2001 (year not leap)
print(next_day(("Wednesday",28,2,2001))) # should print ('Thursday', 1, 3, 2001)
#feb 28 2004 (year leap)
print(next_day(("Saturday",28,2,2004))) # should print ('Sunday', 29, 2, 2004)
print(next_day(("Saturday",21,10,1995))) # should print ('Sunday', 22, 10, 1995)
print(next_day(("Tuesday",31,10,1995))) # should print ('Wednesday', 1, 11, 1995)
print(next_day(("Sunday",31,12,1995))) # should print ('Monday', 1, 1, 1996)
