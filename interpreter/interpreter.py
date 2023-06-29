def main():
    user = input("please enter an arithmetic expression: ")
    x, y, z = user.split(" ")
    x = int(x)
    z = int(z)

    if y == "+":
        print(float(x + z))
    elif y == "-":
        print(float(x - z))
    elif y == "*":
        print(float(x * z))
    elif y == "/":
        print(float(x / z))


main()
