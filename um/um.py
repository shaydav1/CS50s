import re
# import sys


def main():
    print(count(input("Text: ")))


def count(s):
    counter = 0
    words = s.split(' ')
    for word in words:
        matches = re.search(r"(^um$| um\W|^um\W)", word, re.IGNORECASE)
        if matches:
            counter += 1
    return counter


if __name__ == "__main__":
    main()
