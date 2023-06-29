def main():
    user = input("Please enter a string of text: ")
    print(shorten(user))


def shorten(word):
    str_omitted = ""
    for char in word:
        if char.upper() not in ('A', 'E', 'I', 'O', 'U'):
            str_omitted += char
        else:
            str_omitted += ""
    return str_omitted


if __name__ == "__main__":
    main()
