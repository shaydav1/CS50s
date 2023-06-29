def main():
    amount_due = 50
    user = int(input("Insert Coin: "))


    while amount_due > 0:
        if (amount_due - user) == 0:
            amount_due = 0
            print("Change Owed: {}".format(amount_due))
        elif (amount_due - user) < 0:
            amount_due -= user
            print("Change Owed: {}".format(abs(amount_due)))
        elif user in (5, 10, 25):
            amount_due -= user
            print("Amount Due: {}".format(amount_due))
            user = int(input("Insert Coin: "))
        else:
            print("Amount Due: {}".format(amount_due))
            user = int(input("Insert Coin: "))

main()







"""
def main():
    amount_due = 50
    user = int(input("Insert Coin: "))
    while amount_due > 0:
        if user in (5, 10, 25):
            amount_due -= user
            if int(amount_due) <= 0:
                print("Change Owed: {}".format(amount_due))
                break
            print("Amount Due: {}".format(amount_due))
            user = int(input("Insert Coin: "))
        else:
            print("Amount Due: {}".format(amount_due))
            user = int(input("Insert Coin: "))

main()
"""