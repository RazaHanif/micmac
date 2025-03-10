import time
from string import digits, ascii_letters, punctuation
from itertools import product

def four_digit_password():
    for passcode in product(digits, repeat=4):
        print(*passcode)

def four_char_password():
    for passcode in product(ascii_letters, repeat=4):
        print(*passcode)

def four_any_password():
    for passcode in product(ascii_letters + digits + punctuation, repeat=4):
        print(*passcode)

digit_start_time = time.time()
four_digit_password()
digit_time = (time.time() - digit_start_time)

char_start_time = time.time()
four_char_password()
char_time = (time.time() - char_start_time)

any_start_time = time.time()
four_any_password()
any_time = (time.time() - any_start_time)


print("4 Digit time", digit_time)
print("4 Char time", char_time)
print("4 Any time", any_time)
