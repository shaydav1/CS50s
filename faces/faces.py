def main():
    user = input()
    print(convert(user))


def convert(n):
    return n.replace(":)", "🙂").replace(":(", "🙁")


main()
