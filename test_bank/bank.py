def main():
    greeting = input("please enter a greeting! ")
    print("${:.0f}".format(value(greeting)))


def value(greeting):

    if left(greeting.lower().strip(" "), 5) == "hello":
        money = 0
    elif left(greeting, 1).lower() == "h" and left(greeting, 5).lower() != "hello":
        money = 20
    else:
        money = 100

    return money


def left(string, number):
    return string[:number]


if __name__ == "__main__":
    main()
