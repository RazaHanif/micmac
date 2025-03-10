class Account:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, num):
        self._balance += num

    def withdraw(self, num):
        self._balance -= num

    def __str__(self):
        return f"Balance ${self.balance}"

def main():
    account = Account()
    print(account)
    account.deposit(100)
    account.withdraw(50)
    print(account)

if __name__ == "__main__":
    main()