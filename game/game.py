import random


def main():
    while True:
        try:
            level = int(input("Level: "))
            rand = random.randint(1, level)
            if level > 0:
                while True:
                    try:
                        guess = int(input("Guess: "))
                        if 0 < guess <= level:
                            if guess < rand:
                                print("Too small!")
                                continue
                            elif guess > rand:
                                print("Too large!")
                                continue
                            else:
                                print("Just right!")
                            break
                        continue
                    except (TypeError, ValueError):
                        pass
                break
            # else:
        except (TypeError, ValueError):
            pass


if __name__ == "__main__":
    main()
