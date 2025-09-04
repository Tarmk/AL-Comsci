Max = 5
nullPointer = -1
stack = [None] * Max

stack[0] = "Tarm"
stack[1] = "Vivaan"
topPointer = 1  
def pop():
    global Max, nullPointer, topPointer, stack
    if topPointer == nullPointer:
        print("Empty Stack")
    else:
        print(stack[topPointer])
        stack[topPointer] = None
        topPointer -= 1

def push(word):
    global Max, nullPointer, topPointer, stack
    if topPointer == Max - 1:
        print("Stack Full")
    else:
        topPointer += 1
        stack[topPointer] = word

if __name__ == "__main__":
    pop()
    push("Hello")
    push("Hi")
    pop()
    print(stack)



