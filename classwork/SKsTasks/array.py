class Array:
    def __init__(self, capacity):
        self._size = 0
        self._capacity = capacity
        self._element = None
        self.array = [None] * self._capacity

    def is_empty(self):
        return self._size == 0

    def get_size(self):
        return self._size

    def add(self, element):
        for index in range(self._size, self._capacity):
            if self.array[index] is None:
                self.array[index] = element
                self._size += 1
                return element

    def get_element_at_index(self, element_index):
        for index in range(len(self.array)):
            if index == element_index:
                return self.array[index]

    def set_capacity(self, length):
        self._capacity = length

    def get_capacity(self):
        return self._capacity

    def contains(self, element):
        for index in range(self._size):
            if element == self.array[index]:
                return True
            else:
                return False

    def remove(self, element_index):
        for index in range(self._size):
            if index == element_index:
                popped = self.array.pop(index)
                self._size -= 1
                return popped
                # self.array[index] = self.array[index + 1]
                # self._size -= 1
                # return self.array[index]