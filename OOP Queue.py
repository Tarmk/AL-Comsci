class Queue:
    def __init__(self, max_size=5):
        self.max = max_size
        self.data = [None] * max_size
        self.front = 0
        self.rear = -1

    def enqueue(self, item):
        if self.rear == self.max - 1:
            raise IndexError("Queue Full")
        self.rear += 1
        self.data[self.rear] = item
        
    def dequeue(self):
        if self.front == self.rear + 1:
            raise IndexError("Queue Empty")
        item = self.data[self.front]
        self.front += 1
        return item
    
if __name__ == "__main__":
    q = Queue(5)
    q.enqueue("Tarm")
    q.enqueue("Vivaan")
    print(q.dequeue())
    q.enqueue("Hello")
    q.enqueue("Hi")
    print(q.dequeue())
    print(q.dequeue())