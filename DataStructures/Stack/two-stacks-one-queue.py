class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    # populate stack1
    def push(self, x: int) -> None:
        self.stack1.append(x)

    # call peek element, also remove it from stack2
    def pop(self) -> int:
        self.peek()
        return self.stack2.pop()

    # pop from stack1 to stack2, last element will be peek of queue
    def peek(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    # If both stacks are empty then the queue is empty
    def empty(self) -> bool:
        return len(self.stack1) == 0 and len(self.stack2) == 0

def main():
    queue = Queue()
    queue.push(1)
    queue.push(4)
    queue.push(9)
    print(queue.stack1)
    print(queue.pop())
    print(queue.stack1)
    print(queue.stack2)


if __name__ == "__main__":
    main()
