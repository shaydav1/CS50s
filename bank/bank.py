def main():

    greeting = input("please enter a greeting! ")

    if left(greeting.lower().strip(" "), 5) == "hello":
        print ("$0")
    elif left(greeting, 1).lower() == "h" and left(greeting, 5).lower() != "hello":
        print ("$20")
    else:
        print ("$100")


def left(string, number):
    return string[:number]


main()