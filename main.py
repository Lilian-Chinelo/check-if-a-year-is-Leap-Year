def is_leap(year):
  #Docstrings
  """Takes an input as a year and returns if it is a leap year or not."""
  if year < 1:
    return "Invalid Year"
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        print("Leap year.")
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  """Takes two input of year and month and returns the number of days in the chosen month."""
  if month > 12 or month < 1:
    return "Invalid month"
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if is_leap(year) and month == 2:
      return 29
  return month_days[month - 1]
  
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

