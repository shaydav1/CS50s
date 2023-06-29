def main():
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    sum1 = 0
    while True:
        try:
            item = input("Item: ")
        except EOFError:
            print("\n", end="")
            break
        else:
            for x in menu:
                if x.lower() == item.lower():
                    sum1 += menu[x]
                    print("Total: ${:,.2f}".format(sum1))
            else:
                pass


main()
