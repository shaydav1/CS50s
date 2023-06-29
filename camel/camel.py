def main():
    user = input("Write the name of a variable in camel case: ")
    text = ""
    for char in range(len(user)):
        if not user[char].isupper():
            text += user[char]
        else:
            text += '_' + user[char].lower()

    print(text)


main()