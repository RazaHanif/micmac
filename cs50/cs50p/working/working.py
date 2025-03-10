import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # declare vars for later
    start_hour = 0
    start_min = 0
    end_hour = 0
    end_min = 0

    # check if input in correct format (or ValueError)
    if match := re.search(
        r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$",
        s,
    ):
        # start hours
        if match.group(1):
            if 1 <= int(match.group(1)) <= 12:
                if match.group(3) == "AM":
                    if int(match.group(1)) == 12:
                        start_hour = 0
                    else:
                        start_hour = int(match.group(1))
                else:
                    if int(match.group(1)) == 12:
                        start_hour = int(match.group(1))
                    else:
                        start_hour = int(match.group(1)) + 12
            else:
                raise ValueError

        # start mins
        if match.group(2):
            if 0 <= int(match.group(2)) <= 59:
                start_min = int(match.group(2))
            else:
                raise ValueError

        # end hours
        if match.group(4):
            if 1 <= int(match.group(4)) <= 12:
                if match.group(6) == "AM":
                    if int(match.group(4)) == 12:
                        end_hour = 0
                    else:
                        end_hour = int(match.group(4))
                else:
                    if int(match.group(4)) == 12:
                        end_hour = int(match.group(4))
                    else:
                        end_hour = int(match.group(4)) + 12
            else:
                raise ValueError

        # end mins
        if match.group(5):
            if 0 <= int(match.group(5)) <= 59:
                end_min = int(match.group(5))
            else:
                raise ValueError

        return f"{start_hour:02}:{start_min:02} to {end_hour:02}:{end_min:02}"

    else:
        raise ValueError


if __name__ == "__main__":
    main()
