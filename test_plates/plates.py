def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if (s.isalpha() and len_2_6(s)) or (not (
            not first_two_chars(s) or not len_2_6(s) or is_third_char_0(s) or is_last_char_str(s)) and not
                                        is_punctuation(s) and not is_number_in_middle(s)):
        return True
    else:
        return False


def first_two_chars(string):
    if string[0:2].isalpha():
        return True


def len_2_6(string):
    if 2 <= len(string) <= 6:
        return True


def is_third_char_0(string):
    if string[2] == '0':
        return True


def is_last_char_str(string):
    if string[len(string) - 1].isalpha():
        return True


def is_punctuation(string):
    # define punctuation
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for char in string:
        if char in punctuations:
            return True


def is_number_in_middle(string):
    if string[len(string) - 1].isnumeric() and string[len(string) - 2].isalpha():
        return True


if __name__ == "__main__":
    main()
