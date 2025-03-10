import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Check if ip is valid using re
    if bytes := re.search(
        r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$",
        ip,
    ):
        for n in range(4):
            # if any of the bytes arent valid auto fail
            if 0 <= int(bytes.group(n + 1)) <= 255:
                pass
            else:
                return False
        return True
    # if the check is not even possible (alternate entry from user) auto fail
    return False


if __name__ == "__main__":
    main()
