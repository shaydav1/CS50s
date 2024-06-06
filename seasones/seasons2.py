from calendar import leapdays
from datetime import date, datetime
import inflect

p = inflect.engine()


def main():
    start_date = date.today()
    end_date = datetime.strptime(input("Please enter date of birth in 'YYYY-MM-DD' format :"), '%Y-%m-%d').date()

    # Calculating date differences
    day_diff = get_diff(start_date, end_date)

    # Checking for leap days
    leap_days_in_period = leapdays(start_date.year, end_date.year)

    # Calculating minutes in each date part
    day_minutes = day_diff * 24 * 60
    leap_days_minutes = leap_days_in_period * 24 * 60
    minutes = day_minutes + leap_days_minutes

    # print(year_diff, month_diff, day_diff)
    print(p.number_to_words(minutes, andword='').capitalize() + " minutes")


# defining the function for calculating difference between dates
def get_diff(start_date, end_date):
    diff = end_date - start_date
    return diff.days


if __name__ == "__main__":
    main()
