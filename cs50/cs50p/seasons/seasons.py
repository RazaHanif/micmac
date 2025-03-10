import re
import sys
import inflect
from datetime import date


def main():
    birth_date = get_date(input("What is your birth date? YYYY-MM-DD ").rstrip())
    minutes = difference(date.today(), birth_date)
    print(clean_out(minutes))


def get_date(bdate):
    if re.search(r"^\d{4}-\d{2}-\d{2}$", bdate):
        year, month, day = bdate.split("-")
        return date(int(year), int(month), int(day))
    else:
        sys.exit("Format must be: YYYY-MM-DD")


def difference(today, birth):
    if match := re.search(r"^(\d+).*$", str(today - birth)):
        total = int(match.group(1))
        mins = total * 24 * 60
    return mins


def clean_out(num):
    p = inflect.engine()
    return p.number_to_words(num, andword="").capitalize() + " minutes"


if __name__ == "__main__":
    main()
