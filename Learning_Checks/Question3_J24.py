QueueData = [""] * 20
QueueHead = -1
QueueTail = -1
print(QueueData)

def Enqueue(data:str):
    global QueueData, QueueHead, QueueTail
    if QueueTail == 19:
        return False
    if QueueHead == -1:
        QueueHead = 0
        QueueTail = 0
    else:
        QueueTail += 1
    QueueData[QueueTail] = data
    return True

def Dequeue():
    global QueueData, QueueHead, QueueTail
    if QueueHead == -1:
        return "false"
    item = QueueData[QueueHead]
    QueueData[QueueHead] = ""
    if QueueHead == QueueTail:
        QueueHead = -1
        QueueTail = -1
    else:
        QueueHead += 1
    return item

Enqueue("Hello")
Enqueue("Hi")
print(QueueData)
Dequeue()
print(QueueData)