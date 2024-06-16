import sys
import inflect
from calendar import leapdays
from datetime import date, datetime

p = inflect.engine()


def main():
    # Call check_date() function to get the input date components
    date_of_birth_year, date_of_birth_month, date_of_birth_day = check_date(input("Please enter date of birth in "
                                                                                  "'YYYY-MM-DD' format :"))
    # Call today() function to get the current date components
    today_year, today_month, today_day = check_date(input("Please enter date of birth in "
                                                          "'YYYY-MM-DD' format :"))  # today()

    # Calculating date differences
    year_diff = today_year - date_of_birth_year
    month_diff = abs(today_month - date_of_birth_month)
    day_diff = abs(today_day - date_of_birth_day)

    # Checking for leap days
    leap_days_in_period = leapdays(date_of_birth_year, today_year)

    # Calculating minutes in each date part
    year_minutes = year_diff * 365 * 24 * 60
    month_minutes = month_diff * 30 * 24 * 60
    day_minutes = day_diff * 24 * 60
    leap_days_minutes = leap_days_in_period * 24 * 60

    if today_month == date_of_birth_month:
        minutes = year_minutes + month_minutes + day_minutes + leap_days_minutes
    else:
        year_minutes = (year_diff-1) * 365 * 24 * 60
        minutes = year_minutes + month_minutes + day_minutes + leap_days_minutes

    # print(year_diff, month_diff, day_diff)
    print(p.number_to_words(minutes, andword='').capitalize() + " minutes")


# Converting user input to datetime object over string
def check_date(prompt):
    while True:
        try:
            date_of_birth = datetime.strptime(prompt, "%Y-%m-%d")
            date_of_birth_year, date_of_birth_month, date_of_birth_day = date_of_birth.year, date_of_birth.month, \
                date_of_birth.day
            return date_of_birth_year, date_of_birth_month, date_of_birth_day
        except ValueError:
            sys.exit()


# Creating date parts of today
def today():
    today_ = date.today()
    today_year, today_month, today_day = today_.year, today_.month, today_.day
    return today_year, today_month, today_day


# datetime.now().year)
if __name__ == "__main__":
    main()
