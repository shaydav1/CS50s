import re
# import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    matches = re.search(r"/embed/(.+)(\" t|\">)", s, re.IGNORECASE)
    if matches:
        return "https://youtu.be/" + matches.group(1)


if __name__ == "__main__":
    main()
