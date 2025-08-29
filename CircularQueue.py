Max = 5
nullPointer = -1
queue = [None] * Max
itemno = 2

queue[0] = "Tarm"
queue[1] = "Vivaan"

frontPointer = 1
rearPointer = 0

def deque():
    global frontPointer, rearPointer, queue, itemno
    if frontPointer == rearPointer - 1:
        print("Empty queue")
    else:
        item = queue[frontPointer]
        frontPointer = (frontPointer + 1) % Max
        itemno -= 1
        return item
    
def enque(item):
    global frontPointer, rearPointer, queue, itemno
    if itemno == Max:
        print("Full queue")
    else:
        rearPointer = (rearPointer + 1) % Max
        queue[rearPointer] = item
        itemno += 1

    

print(deque())
enque("Hello")
enque("hi")
enque("TJ")
enque("test")
print(deque())
print(deque())
enque("abc")
print(queue)