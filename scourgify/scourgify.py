import sys
import csv


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        scourgify(sys.argv[1], sys.argv[2])


def scourgify(file1, file2):
    try:
        file_list = []
        # open the file and copy the content to a list
        with open(file1) as file1:
            reader = csv.DictReader(file1)
            for row in reader:
                # split name to first name and last name
                last, first = row["name"].split(", ")
                file_list.append({"first": first, "last": last, "house": row["house"]})

        # write list content into a new file
        with open(file2, 'w', newline='') as file2:
            writer = csv.DictWriter(file2, fieldnames=['first', 'last', 'house'])
            writer.writeheader()
            for row1 in file_list:
                writer.writerow(row1)

    except FileNotFoundError:
        sys.exit(f"Could not read {file1}")


if __name__ == "__main__":
    main()
