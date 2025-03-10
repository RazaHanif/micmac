class Wizard:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name

    def __str__(self):
        return f"Wizard: {self.name}"


class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

    def __str__(self):
        return f"Student: {self.name} from house {self.house}"


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def __str__(self):
        return f"Professor: {self.name} teaching {self.subject}"


wiz = Wizard("Albus")
std = Student("Harry", "Ravenclaw")
prof = Professor("Severus", "Potions")

print(wiz)
print(std)
print(prof)