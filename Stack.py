class Stack:
    def __init__(self):
        self.__data = []
        self.top = -1

    def put(self,value):
        self.top += 1
        self.__data[self.top] = value

    def pop(self):
        if self.empty():
            return None

        value = self.__data[self.top]
        self.top -= 1
        return value

    def empty(self):
        return self.top == -1

    def print_all(self):
        for value in self.__data:
            print(value,end=" ")

    def clear(self):
        self.top = -1
        self.__data.clear()

