def main():
    user_time = input("what time is it? ")
    if "a.m." in user_time:
        user_time = convert(user_time.strip(" a.m."))
        if 7.0 <= user_time <= 8.0:
            print("breakfast time")
    elif "p.m." in user_time:
        user_time = convert(user_time.strip(" p.m."))
        if 12.0 <= user_time <= 13.0:
            print("lunch time")
        elif 6.0 <= user_time <= 7.0:
            print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    minutes = int(minutes)/60
    time = float(int(hours)+minutes)
    return time


if __name__ == "__main__":
    main()
