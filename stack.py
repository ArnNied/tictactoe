class StackOverflowException(Exception):
    pass


class StackUnderflowException(Exception):
    def __init__(self, msg="Attempting to retrieve an item from an empty Stack"):
        super().__init__(msg)


class Stack:
    def __init__(self, max_size):
        self.__stack = []
        self.max_size = max_size

    def __str__(self):
        return str(self.__stack)

    def __len__(self):
        return len(self.__stack)

    def is_full(self):
        return len(self.__stack) == self.max_size

    def is_empty(self):
        return len(self.__stack) == 0

    def peek(self):
        if not self.is_empty():
            return self.__stack[-1]
        else:
            raise StackUnderflowException

    def put(self, *values):
        for value in values:
            if not self.is_full():
                self.__stack.append(value)
            else:
                raise StackOverflowException(
                    f"{self.__stack}: {self.max_size} -> Attempting to add an item ({value}) to a full stack"
                )

    def get(self):
        if not self.is_empty():
            return self.__stack.pop(-1)
        else:
            raise StackUnderflowException


# q = Stack(5)
# q.enqueue(1, 2, 3, 4)
# q.peek()
# print(q)
# # q.enqueue(1, 2, 3, 4)
# print(q)

# # print(q.dequeue())
# print(q)
