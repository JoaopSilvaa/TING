from collections import deque


class Queue:
    def __init__(self):
        self._data = deque()

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        if self.__len__ == 0:
            return None
        return self._data.popleft()

    def search(self, index):
        if index > (len(self._data) - 1) or index < 0:
            raise IndexError
        return self._data[index]
