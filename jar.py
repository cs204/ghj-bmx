

class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("The capacity must be a non-negative integer.")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, i):
        if i < 0:
            raise ValueError("The capacity must be a non-negative integer.")
        if self._size + i > self._capacity:
            raise ValueError("Exceeding the jar's capacity.")
        self._size += i

    def withdraw(self, i):
        if i < 0:
            raise ValueError("The number of cookies to remove must be non-negative.")
        if i > self._size:
            raise ValueError("There are not enough cookies in the jar to remove.")
        self._size -= i

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

