class Queue:
    def __init__(self, max_size):
        self.max = max_size
        self.data = [None] * max_size
        self.front = 0
        self.rear = -1
        self.itemno = 0

    def enqueue(self, item):
        if self.itemno == self.max:
            raise IndexError("Queue Full")
        self.rear = (self.rear + 1) % self.max
        self.data[self.rear] = item
        self.itemno += 1

    def dequeue(self):
        if self.front == self.rear + 1:
            raise IndexError("Queue Empty")
        item = self.data[self.front]
        self.front = (self.front + 1) % self.max
        self.itemno -= 1
        return item
    

if __name__ == "__main__":
    q = Queue(5)
    q.enqueue("Tarm")
    q.enqueue("Vivaan")
    q.enqueue("Hello")
    q.enqueue("Hi")
    q.enqueue("TJ")
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    q.enqueue("test")
    q.enqueue("2")
    print(q.dequeue())


