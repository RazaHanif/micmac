class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"Balance:\n{self.galleons} Galleons\n{self.sickles} Sickles\n{self.knuts} Knuts"

    def __add__(self, other):
        g = self.galleons + other.galleons
        s = self.sickles + other.sickles
        k = self.knuts + other.knuts
        return Vault(g, s, k)


def main():
    potter = Vault(100, 50, 25)
    weasley = Vault(25, 50, 100)
    joint = potter + weasley

    print("Welcome to Gringot")
    print("**********")
    print("Potter", potter)
    print("**********")
    print("Weasley", weasley)
    print("**********")
    print("Joint", joint)



if __name__ == "__main__":
    main()