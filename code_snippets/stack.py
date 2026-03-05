# Stack implementation snippet
"""
Stack Data Structure using List
"""

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        print(f"Pushed {item}")

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def display(self):
        print("Stack:", self.items)


def example():
    stack = Stack()

    stack.push(10)
    stack.push(20)
    stack.push(30)

    stack.display()

    print("Top element:", stack.peek())
    print("Popped:", stack.pop())

    stack.display()


if __name__ == "__main__":
    example()
