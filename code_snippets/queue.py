"""
Queue Implementation using List
FIFO Principle
"""

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
        print(f"Enqueued {item}")

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow")
            return None
        return self.items.pop(0)

    def front(self):
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def display(self):
        print("Queue:", self.items)


def run_demo():
    q = Queue()

    q.enqueue(5)
    q.enqueue(15)
    q.enqueue(25)

    q.display()

    print("Front element:", q.front())
    print("Dequeued:", q.dequeue())

    q.display()


if __name__ == "__main__":
    run_demo()
