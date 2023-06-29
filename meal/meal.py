def main():
    user_time = convert(input("what time is it? "))

    if 7.0 <= user_time <= 8.0:
        print("breakfast time")
    elif 12.0 <= user_time <= 13.0:
        print("lunch time")
    elif 18.0 <= user_time <= 19.0:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    minutes = int(minutes)/60
    time = float(int(hours)+minutes)
    return time


if __name__ == "__main__":
    main()
