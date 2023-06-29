def main():
    list1 = {}
    while True:
        try:
            item = input()
            if item.lower() in list:
                list1[item] += 1
            else:
                list1[item] = 1
        except EOFError:
            for item, count in sorted(list1.items()):
                print(count, item.upper())
            break


main()
