size = 10 + 1
cq = [0] * size
front = rear = 0


def isFull():
    return (rear + 1)%size == front

def enqueue(item):
    global rear
    if isFull():
        print("full")
        return
    rear = (rear + 1) % size
    cq[rear] = item

def dequeue():
    global front
    if isEmpty():
        print("Empty")
        return
    front = (front+1) % size
    return cq[front]

def isEmpty():
    return front == rear

for i in range(10):
    enqueue(i)

print(cq)
print(isFull())
print(isEmpty())

for i in range(10):
    print(dequeue(), end=" ")
print()
print(isEmpty())
print(isFull())
print(cq)

