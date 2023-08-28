import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    conversion_table = {'12:00 AM': '00:00',
                        '1:00 AM': '01:00',
                        '2:00 AM': '02:00',
                        '3:00 AM': '03:00',
                        '4:00 AM': '04:00',
                        '5:00 AM': '05:00',
                        '6:00 AM': '06:00',
                        '7:00 AM': '07:00',
                        '8:00 AM': '08:00',
                        '9:00 AM': '09:00',
                        '10:00 AM': '10:00',
                        '11:00 AM': '11:00',
                        '12:00 PM': '12:00',
                        '1:00 PM': '13:00',
                        '2:00 PM': '14:00',
                        '3:00 PM': '15:00',
                        '4:00 PM': '16:00',
                        '5:00 PM': '17:00',
                        '6:00 PM': '18:00',
                        '7:00 PM': '19:00',
                        '8:00 PM': '20:00',
                        '9:00 PM': '21:00',
                        '10:00 PM': '22:00',
                        '11:00 PM': '23:00'}
    try:
        matches = re.search(r"(0?[1-9]:?[:0-5]?[0-9]? [AaPp][Mm]|1[0-2]:?[:0-5]?[0-9]? [AaPp][Mm]) to (0?[1-9]:?["
                            r":0-5]?[0-9]? [AaPp][Mm]|1[0-2]:?[:0-5]?[0-9]? [AaPp][Mm])", s, re.IGNORECASE)
        begin_hour, end_hour = matches.group(1), matches.group(2)
        for hour in conversion_table:
            if begin_hour == hour or begin_hour == (hour[0:2] + ' ' + hour[-2:]) or \
                    begin_hour == (hour[0:1] + ' ' + hour[-2:]) or \
                    (begin_hour[0:2] == hour[0:2] and begin_hour[-2:] == hour[-2:]):
                if ':' not in begin_hour:
                    begin_hour = conversion_table[hour]
                elif begin_hour[-5:-3] != '00':
                    minutes = begin_hour[-5:-3]
                    begin_hour = conversion_table[hour][0:2] + ':' + minutes
                else:
                    begin_hour = conversion_table[hour]
            if end_hour == hour or end_hour == (hour[0:2] + ' ' + hour[-2:]) or \
                    end_hour == (hour[0:1] + ' ' + hour[-2:]) or \
                    (end_hour[0:2] == hour[0:2] and end_hour[-2:] == hour[-2:]):
                if ':' not in end_hour:
                    end_hour = conversion_table[hour]
                elif end_hour[-5:-3] != '00':
                    minutes = end_hour[-5:-3]
                    end_hour = conversion_table[hour][0:2] + ':' + minutes
                else:
                    end_hour = conversion_table[hour]
        return f"{begin_hour:02}" + " to " + f"{end_hour:02}"
    except AttributeError:
        raise ValueError


if __name__ == "__main__":
    main()
