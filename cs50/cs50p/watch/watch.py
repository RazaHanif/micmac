import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if match := re.search(
        r"^<iframe.*src=.*(?:https?://)?(?:www\.)?youtube\.com/embed/([\w]+).*</iframe>$",
        s,
        re.IGNORECASE,
    ):
        return f"https://youtu.be/{match.group(1)}"


if __name__ == "__main__":
    main()
