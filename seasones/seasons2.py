import sys
from datetime import date, datetime


def main():
    # Call check_date() function to get the input date components
    date_of_birth_year, date_of_birth_month, date_of_birth_day = check_date(input("Please enter date of birth in "
                                                                                  "'YYYY-MM-DD' format :"))
    # Call today() function to get the current date components
    today_year, today_month, today_day = today()
    year_diff = today_year - date_of_birth_year
    month_diff = abs(today_month - date_of_birth_month)
    day_diff = abs(today_day - date_of_birth_day)
    print(year_diff, month_diff, day_diff)


# converting user input to datetime object over string
def check_date(prompt):
    while True:
        try:
            date_of_birth = datetime.strptime(prompt, "%Y-%m-%d")
            date_of_birth_year, date_of_birth_month, date_of_birth_day = date_of_birth.year, date_of_birth.month, \
                date_of_birth.day
            return date_of_birth_year, date_of_birth_month, date_of_birth_day
        except ValueError:
            sys.exit()


# creating date parts of today
def today():
    today_ = date.today()
    today_year, today_month, today_day = today_.year, today_.month, today_.day
    return today_year, today_month, today_day


# datetime.now().year)
if __name__ == "__main__":
    main()
