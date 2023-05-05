class Queue:
 def __init__(self):
     self.items = []
 def is_empty(self):
         return len(self.items) == 0
 def enqueue(self,item):
     self.items.append(item)
 def dequeue(self):
     if self.is_empty():
        return None
     return self.items.pop(0)
 def peek(self):
     if self.is_empty():
        return None
     return self.items[0]
 def size(self):
     return len(self.items)
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.size()) 
print(q.dequeue()) 
print(q.dequeue()) 
print(q.peek()) 
