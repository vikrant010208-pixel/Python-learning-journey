import calendar

# Generate calender
Year = int(input("Enter the year: "))
Month = int(input("Enter the month: "))

calendar_Generator = calendar.month(Year, Month)

print(calendar_Generator)