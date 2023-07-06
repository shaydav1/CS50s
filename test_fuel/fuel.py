def main():
    frac = convert(input("Fraction: "))
    print(gauge(frac))


def convert(fraction):
    while True:
        fraction = fraction.split("/")
        try:
            x, y = int(fraction[0]), int(fraction[1])
            fuel = int(round(x / y, 2) * 100)
            if fuel > 100:
                fraction = input("Fraction: ")
            else:
                return fuel
        except (IndexError, ValueError, ZeroDivisionError):
            fraction = input("Fraction: ")


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        ans = str(percentage) + '%'
        return str(ans)


if __name__ == "__main__":
    main()
