import random


# You can create class variables, and methods without creating an instance the class
class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    # dont need to include self, instead call the class with cls
    @classmethod
    def sort(cls, name):
        print(f"{name} is in house {random.choice(cls.houses)}")


#  just call and use the class + method without creaing an instance of the class
def main():
    Hat.sort("Harry")


if __name__ == "__main__":
    main()