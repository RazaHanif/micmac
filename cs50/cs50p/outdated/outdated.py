def main():
    months = {
        "January": "1",
        "February": "2",
        "March": "3",
        "April": "4",
        "May": "5",
        "June": "6",
        "July": "7",
        "August": "8",
        "September": "9",
        "October": "10",
        "November": "11",
        "December": "12"
    }

    while True:

        date = input("Date: ").strip()

        try:
            month, day, year = date.split("/")
        except ValueError:
            for key in months:
                if date.startswith(key):
                    try:
                        temp, year = date.split(",")
                    except ValueError:
                        pass
                    else:
                        month, day = temp.split(" ")
                        month = months[key]
        try:
            year = year.strip()
            month = pre(month)
            day = pre(day)
        except (UnboundLocalError, ValueError):
            pass
        else:
            if 1 <= int(month) <= 12:
                if 1 <= int(day) <= 31:
                    break


    print(year + "-" + month + "-" + day)

def pre(num):
    if 0 < int(num) < 10:
        return "0" + num
    else:
        return num

main()