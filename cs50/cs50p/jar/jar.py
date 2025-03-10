class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("capacity cannot be negative")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if (self.size + n) > self.capacity:
            raise ValueError("Jar Overflown")
        self.size = self.size + n

    def withdraw(self, n):
        if self.size < n:
            raise ValueError("Jar doesnt have overdraft")
        self.size = self.size - n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, num):
        if num < 0:
            raise ValueError("capacity cannot be negative")
        self._capacity = num

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, num):
        self._size = num
