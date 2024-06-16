# ChatGPT
import sys
from datetime import date, datetime
import inflect

p = inflect.engine()


def main():
    try:
        # Accepting date of birth from the user
        start_date = get_date_of_birth()
        end_date = date.today()

        # Calculating date differences in days and converting to minutes
        day_diff = get_diff(start_date, end_date)
        minutes = day_diff * 24 * 60

        # Printing the result in words
        print(p.number_to_words(minutes, andword='').capitalize() + " minutes")

    except ValueError as e:
        sys.exit(f"Error: {e}")


def get_date_of_birth():
    """
    Prompt the user to enter their date of birth and return it as a date object.
    Raises a ValueError if the input format is incorrect.
    """
    dob_str = input("Please enter date of birth in 'YYYY-MM-DD' format: ")
    try:
        return datetime.strptime(dob_str, '%Y-%m-%d').date()
    except ValueError:
        raise ValueError("Wrong date format. Please enter date in 'YYYY-MM-DD' format.")


def get_diff(start_date, end_date):
    """
    Calculate the difference between two dates in days.

    Parameters:
    start_date (date): The start date.
    end_date (date): The end date.

    Returns:
    int: The number of days between the two dates.
    """
    diff = end_date - start_date
    return diff.days


if __name__ == "__main__":
    main()
