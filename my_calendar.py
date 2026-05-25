import calendar

year = int(input("Please Enter the year: "))
month = int(input("Please Enter month: "))
cal = calendar.month(year, month)
print(cal)