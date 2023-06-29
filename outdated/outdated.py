def main():
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    while True:
        try:
            date = input("Date: ")
            if "/" in date:
                date = date.split("/")
                if len(date[0].strip()) < 2:
                    date[0] = "0" + date[0].strip()
                if len(date[1].strip()) < 2:
                    date[1] = "0" + date[1].strip()
                if int(date[1]) <= 31 and int(date[0]) <= 12:
                    date = date[2].strip() + "-" + date[0] + "-" + date[1]
                    print(date)
                    break
                else:
                    pass
            elif "," in date:
                date = date.split(",")  # splitting by ","
                year = date[1].strip()  # striping the backspace
                month, day = date[0].split(" ")  # splitting by backspace
                month = str(months.index(month) + 1)  # taking the month index from months list plus 1
                if len(month) < 2:
                    month = "0" + month
                if len(day) < 2:
                    day = "0" + day
                if int(day) <= 31 and int(month) <= 12:
                    date = year + "-" + month + "-" + day
                    print(date)
                    break
                else:
                    pass
        except IndexError:
            pass
        except ValueError:
            pass


main()
