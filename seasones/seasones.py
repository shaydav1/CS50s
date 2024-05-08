import sys
from datetime import date, datetime


def main():
    dob_list = check_date(input("Please enter date of birth in 'YYYY-MM-DD' format :"))
    year_diff = today_date()[0] - dob_list[0]
    month_diff = abs(today_date()[1] - dob_list[1])
    day_diff = abs(today_date()[2] - dob_list[2])
    print(year_diff, month_diff, day_diff)


# converting user input to datetime object over string

def check_date(prompt):
    while True:
        try:
            date_of_birth = datetime.strptime(prompt, "%Y-%m-%d")
            dob = [int(date_of_birth.year), int(date_of_birth.month), int(date_of_birth.day)]
            return dob
        except ValueError:
            sys.exit()


# creating date parts of today

def today_date():
    today = date.today()
    today = [int(today.year), int(today.month), int(today.day)]
    return today


if __name__ == "__main__":
    main()
