
class stack:
    def __init__(self, max_size=5):
        self.max= max_size
        self.data = [None] * max_size
        self.top = -1


    def push(self, item):
        if self.top == self.max - 1:
            raise IndexError("Stack Full")
        self.top += 1
        self.data[self.top] = item


    def pop(self):
        if self.top == -1:
            raise IndexError("Empty Stack")
        item = self.data[self.top]
        self.data[self.top] = None
        self.top -=1
        return item
    
if __name__ == "__main__":
    s = stack(5)
    s.push("Tarm")
    s.push("Vivaan")
    print(s.pop())     
    s.push("Hello")
    s.push("Hi")
    print(s.pop())    
    print(s)