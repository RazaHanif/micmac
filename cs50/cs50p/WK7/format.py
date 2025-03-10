import re

name = input("Whats your name? ").strip()

# := lets you assign, and check for an if statment
if match := re.search(r"^(.+), *(.+)$", name, re.IGNORECASE):
    name = match.group(2).strip() + " " + match.group(1).strip()

print(f"Hello, {name}")