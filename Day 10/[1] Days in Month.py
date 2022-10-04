MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year:int, month:int) -> int:
    if 1 > month > 12:
        return 'Invalid input!'
    isLeapYear = is_leap(year)
    if isLeapYear:
        feb = 29
    else:
        feb = 28

    month_days = [31, feb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return month_days[month-1]

#🚨 Do NOT change any of the code below
year = int(input("Enter year: "))
month = int(input("Enter month: "))
days = days_in_month(year, month)
print(f'There are {days} days in month of {MONTHS[month-1]} of year {year}.')
