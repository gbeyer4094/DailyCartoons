from datetime import datetime, date

def days_left_in_year():
    today = date.today()
    day_of_year = datetime(today.year,today.month,today.day).timetuple().tm_yday
    end_of_year = datetime(today.year,12,31).timetuple().tm_yday
    return end_of_year - (day_of_year +1)


current = int(input('Current number of Steps: '))
days_left = days_left_in_year()
remaining = (8000000 - current)/days_left
print(remaining)
