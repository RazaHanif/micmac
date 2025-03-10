# Creating classes in python
class Student:
    # initalize a default constructor
    # house=None gives a default value
    def __init__(self, name, house):
        self.name = name
        self.house = house

    # special class methods, anytime another method wants to see object as string
    def __str__(self):
        return f"{self.name} from house {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)

        # return cls(input("name: "), input("house: "))

    # decorator allows you to define getter/setter methods
    # @property = getter
    # @var.setter = setter

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name


    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self._house = house


# can use tuples to send multiple items (kinda like an array)
# tuple values cannot be reassigned
# if you need the vars to be mutable (changeable) make them a list
# return (name, house) == tuple
# return [name, house] == list

def main ():
    print(Student.get())


if __name__ == "__main__":
    main()