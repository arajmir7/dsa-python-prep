class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, x):
        self.queue.append(x)

    def dequeue(self):
        if not self.isEmpty():
            return self.queue.pop(0)
        return "Queue is empty"

    def front(self):
        if not self.isEmpty():
            return self.queue[0]
        return "Queue is empty"

    def isEmpty(self):
        return len(self.queue) == 0


q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Front:", q.front())
print("Dequeued:", q.dequeue())
print("Front after dequeue:", q.front())