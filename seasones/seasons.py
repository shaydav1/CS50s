import sys
from datetime import date, datetime
import inflect

p = inflect.engine()


def main():
    try:
        # Accepting parameters from the user
        start_date = datetime.strptime(input("Please enter date of birth in 'YYYY-MM-DD' format :"), '%Y-%m-%d').date()
        end_date = date.today()

        # Calculating date differences in days and translate it to units of minutes, then print it
        day_diff = get_diff(start_date, end_date)
        minutes = day_diff * 24 * 60
        print(p.number_to_words(minutes, andword='').capitalize() + " minutes")

    except ValueError:
        sys.exit("Wrong date format")


# Defining the function for calculating difference between dates
def get_diff(start_date, end_date):
    diff = end_date - start_date
    return diff.days


if __name__ == "__main__":
    main()
