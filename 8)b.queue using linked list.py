class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        item = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return item

    def peek(self):
        if self.is_empty():
            return None
        return self.head.data

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

# Example usage
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.size())  # Output: 3
print(q.dequeue())  # Output: 1
print(q.dequeue())  # Output: 2
print(q.peek())  # Output: 3
