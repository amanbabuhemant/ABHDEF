def is_leap_year(year):
    if not year % 100:
        return not year % 400
    return not year % 4
