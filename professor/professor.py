import random


def main():
    # Prompts the user for a level, n. If the user does not input 1, 2, or 3, the program should prompt again.
    level = get_level()
    i = 0
    correct_answers = 0
    # Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative
    # integer with n digits. No need to support operations other than addition (+).
    while i < 10:
        i += 1
        x = generate_integer(level)
        y = generate_integer(level)
        z = int(x + y)
        # Prompts the user to solve each of those problems.
        # If an answer is not correct (or not even a number), the program should output EEE and prompt the user again,
        # allowing the user up to three tries in total for that problem. If the user has still not answered
        # correctly after three tries, the program should output the correct answer.
        question = int(input("{} + {} = ".format(x, y)))
        if question == z:
            correct_answers += 1
            continue

        elif question != z:
            false_answer_counter = 0
            while question != z:
                false_answer_counter += 1
                if false_answer_counter == 3:
                    print("{} + {} = {}".format(x, y, z))
                    break
                else:
                    print("EEE")
                    question = int(input("{} + {} = ".format(x, y)))

    # The program should ultimately output the user’s score: the number of correct answers out of 10.
    print(correct_answers)


# get_level prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3
def get_level():
    while True:
        level = int(input("Level: "))
        if 1 <= level <= 3:
            return level
        else:
            continue


# generate_integer returns a randomly generated non-negative integer with level digits or raises a ValueError if
# level is not 1, 2, or 3
def generate_integer(level):
    try:
        if level == 1:
            return random.randrange(0, 9)
        elif level == 2:
            return random.randrange(10, 99)
        else:
            return random.randrange(100, 999)
    except ValueError:
        raise ValueError


if __name__ == "__main__":
    main()
