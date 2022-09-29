#!/usr/bin/env python3

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.tail = None
    
    # Time: O(1) / Space: O(1)
    def empty(self) -> bool:
        return self.tail == None
    
    # Time: O(1) / Space: O(1)
    def append(self, data):
        new_node = Node(data)
        if self.empty():
            self.tail = new_node
            self.tail.next = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node
    
    # Time: O(1) / Space: O(1)
    def insert(self, data) -> None:
        new_node = Node(data)
        if self.empty():
            self.tail = new_node
            self.tail.next = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node

    # Time: O(n) / Space: O(1)
    def contains(self, data) -> bool:
        # No nodes
        if self.empty():
            return
        current_node = self.tail.next
        start_node = current_node
        while True:
            if current_node.value == data:
                return True
            current_node = current_node.next
            if current_node == start_node:
                break
        return False
    
    # Time: O(1) / Space: O(1)
    def deleteFrontNode(self):
        # No nodes
        if self.empty():
            return
        # One node
        elif self.tail == self.tail.next:
            self.tail = None
        # Multi nodes
        else:
            to_be_head_node = self.tail.next.next
            self.tail.next = to_be_head_node
        
    # Time: O(n) / Space: O(1)
    def deleteRearNode(self):
        # No nodes
        if self.empty():
            return
        # One node
        elif self.tail == self.tail.next:
            self.tail = None
        # Multi nodes
        else:
            current_node = self.tail.next
            to_be_tail_node = None
            while True:
                current_node = current_node.next
                if current_node.next == self.tail:
                    current_node.next = self.tail.next
                    self.tail = current_node
                    break
    
    # Time: O(n) / Space: O(1)
    def deleteNodeByKey(self, key):
        # No nodes
        if self.empty():
            return
        # If the key holds 1st node
        current_node = self.tail.next

        if current_node.value == key:
            self.deleteFrontNode()
            return
        
        start_node = current_node
        while True:
            # If to be deleted node is non-head, non-tail
            if current_node.value == key:
                current_node.value = current_node.next.value
                current_node.next = current_node.next.next
                return
            # If to be deleted node is the tail node
            if current_node.next.value == key and current_node.next == self.tail:
                current_node.next = self.tail.next
                self.tail = current_node
                return
            current_node = current_node.next
            if current_node == start_node:
                break
 
    # Time: O(n) / Space: O(1)
    def print(self) -> None:
        if self.tail == None:
            print('[]')
            return
        print('[',end='')
        current_node = self.tail.next
        start_node = current_node
        while True:
            print(current_node.value,end=' ')
            current_node = current_node.next
            if current_node == start_node:
                break
        print(']\n',end='')

def main():
    CLL = CircularLinkedList()
    CLL.append(5); CLL.append(2); CLL.append(3); CLL.append(4)
    print(CLL.contains(21)) # False
    print(CLL.contains(5)) # True
    CLL.print() # [5 2 3 4 ]
    CLL.deleteNodeByKey(5)
    CLL.deleteNodeByKey(2)
    CLL.print() # [3 4]
    CLL.deleteFrontNode()
    CLL.deleteRearNode()
    CLL.print() # []



if __name__ == "__main__":
    main()
