from datetime import datetime

Gregorian_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def leap_year(birth_year, current_year):
    count = 0
    for y in range(birth_year, current_year + 1):
        if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
            count += 1
    return count

def to_days(age, birth_year, birth_month, birth_day, today):
    ty, tm, td = today
    
    days = age[0] * 365
    
    days += leap_year(birth_year, ty)
    
    for m in range(age[1]):
        days += Gregorian_month[m]
    
    days += age[2]
    return days

def to_hours(days):
    return days * 24

def to_sec(days):
    return days * 24 * 3600

def calculate_age(birth, today):
    by, bm, bd = birth
    ty, tm, td = today
    years = ty - by
    months = tm - bm
    days = td - bd
    if days < 0:
        months -= 1
       
        prev_month = (tm - 2) % 12
        days += Gregorian_month[prev_month]
    if months < 0:
        years -= 1
        months += 12
    return [years, months, days]

today_time = [int(x) for x in datetime.today().strftime('%Y-%m-%d').split("-")]

while True:
    temp = int(input("Enter 1 for age, 2 for birth date: "))
    if temp == 1:
        years = int(input("Enter your age: "))
        age = [years, 0, 0]
        birth_year = today_time[0] - years
        birth_month = today_time[1]
        birth_day = today_time[2]
        break
    elif temp == 2:
        while True:
            raw = input("Enter birth date (YYYY-MM-DD): ").split("-")
            if len(raw) == 3 and all(p.isdigit() for p in raw):
                y, m, d = map(int, raw)
                if 1 <= m <= 12 and 1 <= d <= 31:
                    birth_year, birth_month, birth_day = y, m, d
                    age = calculate_age([y, m, d], today_time)
                    break
                else:
                    print("Invalid month or day.")
            else:
                print("Invalid format.")
        break
    else:
        print("Invalid choice.")

months = age[0] * 12 + age[1]
days = to_days(age, birth_year, birth_month, birth_day, today_time)
hours = to_hours(days)
seconds = to_sec(days)

print('You are %d years, %d months, and %d days old.' % (age[0], age[1], age[2]))
print('Equals to %d months, %d days, %d hours, %d seconds.' % (months, days, hours, seconds))