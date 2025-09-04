Max = 5
nullPointer = -1
queue = [None] * Max

queue[0] = "Tarm"
queue[1] = "Vivaan"

frontPointer = 1
rearPointer = 0

def deque():
    global frontPointer, rearPointer, queue
    if frontPointer == rearPointer - 1:
        print("Empty queue")
    else:
        frontPointer += 1
        queue[frontPointer - 1] = None
        return (queue[frontPointer - 1])
    
def enque(item):
    global frontPointer, rearPointer, queue
    if frontPointer == rearPointer - 1:
        print("Full queue")
    else:
        rearPointer += 1
        queue[rearPointer] = item

if __name__ == "__main__":
    print(deque())
    print(queue)
    enque("Hello")
    print(queue)
    enque("hi")



