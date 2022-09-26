#!/usr/bin/env python3
'''
List implementation of the Queue impedes performance executing deque operation.
Removing an element from beginning of the list results all the other elements
to shift left by one, which requires linear time. list.pop(0) = Time O(n)
'''
class Queue:
    def __init__(self) -> None:
        self.elements = []

    # Time: O(1) / Space: O(1)
    def enqueue(self, element) -> None:
        self.elements.append(element)

    # Time: O(n) / Space: O(1)
    def dequeue(self):
        if self.empty():
            return None
        return self.elements.pop(0)

    # Time: O(1) / Space: O(1)
    def size(self) -> int:
        return len(self.elements)

    # Time: O(1) / Space: O(1)
    def empty(self):
        return False if self.size() else True

    # Time: O(1) / Space: O(1)
    def peek(self):
        if self.empty():
            return None
        return self.elements[0]

    # Time: O(1) / Space: O(1)
    def rear(self):
        if self.empty():
            return None
        return self.elements[-1]

    # Time: O(n) / Space: O(1)
    def print(self) -> None:
        _size = self.size()
        for _ in range(_size):
            _elem = self.dequeue()
            print(_elem, end=' ')
            self.enqueue(_elem)
        print()

    # Time: O(n) / Space: O(1)
    def contains(self, data) -> bool:
        _size = self.size()
        doesContain = False
        for _ in range(_size):
            _elem = self.dequeue()
            if _elem == data:
                doesContain = True
            self.enqueue(_elem)
        return doesContain

def main():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(4)
    queue.enqueue(9)
    queue.print()
    print(queue.contains(3))
    print(queue.contains(1))
    print(queue.rear())
    print(queue.peek())
    queue.dequeue()
    queue.print()
    queue.enqueue(2)
    queue.print()


if __name__ == "__main__":
    main()