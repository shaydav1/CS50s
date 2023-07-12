import sys


def main():
    # If the user does not specify exactly one command-line argument
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        # if the specified file’s name does not end in .py
        file = sys.argv[1]
        if not file.endswith('.py'):
            sys.exit("Not a Python file")
        else:
            # go count rows
            print(count_rows_in_file(file))


def count_rows_in_file(file):
    try:
        # if the specified file does not exist
        with open(file, "r") as file:
            lines = file.readlines()
            counter = 0
            for line in lines:
                # Assume that any line that only contains whitespace is blank.
                if line.isspace():
                    pass
                # Assume that any line that starts with #, optionally preceded by whitespace, is a comment.
                elif line.lstrip().startswith("#"):
                    pass
                else:
                    counter += 1
            return counter
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
