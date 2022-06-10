class QueueOverflowException(Exception):
    pass


class QueueUnderflowException(Exception):
    def __init__(self, msg="Attempting to retrieve an item from an empty queue"):
        super().__init__(msg)


class Queue:
    def __init__(self, max_size):
        self.__queue = []
        self.max_size = max_size

    def __str__(self):
        return str(self.__queue)

    def __len__(self):
        return len(self.__queue)

    def is_full(self):
        return len(self.__queue) >= self.max_size

    def is_empty(self):
        return len(self.__queue) == 0

    def peek(self):
        if not self.is_empty():
            return self.__queue[0]
        else:
            raise QueueUnderflowException

    def enqueue(self, *values):
        for value in values:
            if not self.is_full():
                self.__queue.append(value)
            else:
                raise QueueOverflowException(
                    f"{self.__queue}: {self.max_size} -> Attempting to add an item ({value}) to a full queue"
                )

    def dequeue(self):
        if not self.is_empty():
            return self.__queue.pop(0)
        else:
            raise QueueUnderflowException


# q = Queue(5)
# q.enqueue(1, 2, 3, 4, 1)
# a = q.dequeue()
# print(a)
# q.peek()
# print(q)
# # q.enqueue(1, 2, 3, 4)
# print(q)

# # print(q.dequeue())
# print(q)

# q = Queue(10)

# print(q)
# q.enqueue({"nama": "Andrien", "kelamin": "L"})
# print(q)
# q.enqueue({"nama": "Aznal", "kelamin": "L"})
# print(q)

# proses1 = q.dequeue()
# print(q)
# proses2 = q.dequeue()
# print(q)
