def is_leap(year):
    leap = False

    if 1900<=year<=10**5:
        if year%4==0:
            if year%100==0 & year%