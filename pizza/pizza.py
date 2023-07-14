import sys
import os
from tabulate import tabulate
import csv


def main():
    # If the user does not specify exactly one command-line argument, the program should instead exit via sys.exit.
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        # If the specified file’s name does not end in .csv, the program should instead exit via sys.exit.
        file = sys.argv[1]
        if not file.endswith(".csv"):
            sys.exit("Not a CSV file")
        # If the specified file does not exist, the program should instead exit via sys.exit.
        elif not os.path.exists(file):
            sys.exit("File does not exist")
        else:
            print(table(file))


def table(csv_file):
    try:
        with open(csv_file) as file:
            reader = csv.reader(file)
            return tabulate(reader, headers='first-row', tablefmt='grid')
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
