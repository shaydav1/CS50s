def main():
    user = input("Please enter a string of text: ")

    """
    # new_str = ""
    for char in user:
        if char.upper() not in ('A', 'E', 'I', 'O', 'U'):
            new_str += char
        else:
            new_str += ""
    """
    print(vowels_omitter(user))


def vowels_omitter(str1):
    str_omitted = ""
    for char in str1:
        if char.upper() not in ('A', 'E', 'I', 'O', 'U'):
            str_omitted += char
        else:
            str_omitted += ""
    return str_omitted


main()
