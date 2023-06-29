import inflect

p = inflect.engine()


def main():
    list = []
    try:
        while True:
            list.append(str(input()))
    except EOFError as e:
        print("Adieu, adieu, to", p.join(list))


if __name__ == "__main__":
    main()
