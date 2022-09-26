#!/usr/bin/env python3
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LLQueue:
    def __init__(self):
        self.head = self.tail = None

    # Time: O(1) / Space: O(1)
    def enqueue(self, data) -> None:
        new_node = Node(data)
        if self.empty():
           self.head = self.tail = new_node
           return
        self.tail.next = new_node
        self.tail = new_node

    # Time: O(1) / Space: O(1)
    def dequeue(self):
        if self.empty():
            return None
        del_elem = self.head.value
        self.head = self.head.next
        return del_elem

    # Time: O(1) / Space: O(1)
    def empty(self):
        return self.head == None

    # Time: O(1) / Space: O(1)
    def peek(self):
        if self.empty():
            return  None
        return self.head.value

    # Time: O(1) / Space: O(1)
    def rear(self):
        if self.empty():
            return  None
        return self.tail.value

    # Time: O(n) / Space: O(1)
    def print(self) -> None:
        print('[',end='')
        tmp_head = self.head
        while self.head != None:
            print(self.head.value, end=' ')
            self.head = self.head.next
        print(']\n',end='')
        self.head = tmp_head

    # Time: O(n) / Space: O(1)
    def contains(self, data) -> bool:
        doesContain = False
        tmp_head = self.head
        while self.head != None:
            if self.head.value == data:
                doesContain = True
            self.head = self.head.next
        self.head = tmp_head
        return doesContain

def main():
    queue = LLQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    print(queue.contains(2)) # True
    print(queue.contains(5)) # False
    queue.enqueue(3)
    queue.enqueue(4)
    queue.print()   # [1 2 3 4 ]
    queue.dequeue()
    queue.print()   # [2 3 4 ]
    queue.enqueue(5)
    queue.print() # [2 3 4 5 ]
    print(queue.rear()) # 5
    print(queue.peek()) # 2
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    print(queue.rear()) # 5
    print(queue.peek()) # 5
    queue.dequeue()
    queue.print() # []
    print(queue.rear()) # None
    print(queue.peek()) # None
    print()


if __name__ == "__main__":
    main()