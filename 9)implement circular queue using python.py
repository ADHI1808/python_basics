class CircularQueue:
    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = -1
        self.tail = -1

    def is_empty(self):
        return self.head == -1

    def is_full(self):
        return (self.tail + 1) % self.k == self.head

    def enqueue(self, item):
        if self.is_full():
            return False
        if self.is_empty():
            self.head = 0
        self.tail = (self.tail + 1) % self.k
        self.queue[self.tail] = item
        return True

    def dequeue(self):
        if self.is_empty():
            return None
        item = self.queue[self.head]
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
        else:
            self.head = (self.head + 1) % self.k
        return item

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[self.head]

    def size(self):
        if self.is_empty():
            return 0
        elif self.is_full():
            return self.k
        else:
            return (self.tail - self.head + self.k) % self.k + 1

# Example usage
q = CircularQueue(3)
print(q.enqueue(1))  # Output: True
print(q.enqueue(2))  # Output: True
print(q.enqueue(3))  # Output: True
print(q.enqueue(4))  # Output: False
print(q.peek())  # Output: 1
print(q.size())  # Output: 3
print(q.dequeue())  # Output: 1
print(q.dequeue())  # Output: 2
print(q.enqueue(4))  # Output: True
print(q.peek())  # Output: 3
print(q.size())  # Output: 2
