def main():
    x = check_fraction("Fraction: ")
    if x >= 0.99:
        print("F")
    elif x <= 0.01:
        print("E")
    else:
        print("{0:.0%}".format(x))


def check_fraction(prompt):
    while True:
        try:
            fraction = input(prompt).split("/")
            x, y = int(fraction[0]), int(fraction[1])
            answer = x / y
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        else:
            if x / y > 1:
                pass
            else:
                return answer


main()

"""
def main():
    while True:
        try:
            fraction = input("Fraction: ").split("/")
            X, Y = int(fraction[0]), int(fraction[1])
            answer = X/Y
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        else:
            if X/Y > 1:
                pass
            else:
                break

    if answer >=0.99:
        print("F")
    elif answer <= 0.01:
        print("E")
    else:
        print ("{0:.0%}".format(answer))

main()
"""
