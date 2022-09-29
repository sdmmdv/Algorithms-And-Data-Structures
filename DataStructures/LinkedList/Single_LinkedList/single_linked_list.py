#!/usr/bin/env python3

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Time: O(1) / Space: O(n)
    def append(self, data) -> None:
        if not self.head:
            self.head = Node(data)
        else:
            current_node = self.head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = Node(data)

    # Time: O(1) / Space: O(1)
    def insert(self, data) -> None:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    # Time: O(n) / Space: O(1)
    def contains(self, data) -> bool:
        current_node = self.head
        while current_node != None:
            if current_node.value == data:
                return True
            current_node = current_node.next
        return False

    # Time: O(1) / Space: O(1)
    def empty(self) -> bool:
        return self.head == None

    # Time: O(1) / Space: O(1)
    def deleteFrontNode(self) -> None:
        if self.empty():
            return
        if self.head.next == None:
            self.head = None
        else:
            self.head.value = self.head.next.value
            self.head.next = self.head.next.next

    # Time: O(n) / Space: O(1) 
    def deleteRearNode(self) -> None:
        if self.empty():
            return
        if self.head.next == None:
            self.head = None
            return

        current_node = self.head
        while current_node.next != None:
            # If it's the tail node
            if current_node.next.next == None:
                current_node.next = None
                return
            current_node = current_node.next



    # In addition to current node, track the previous 
    # node if to be deleted node is the latest (tail node)
    # Time: O(n) / Space: O(1)
    def deleteNodeWithPrev(self, key) -> None:
        if self.empty():
            return
        current_node = self.head
        prev_node = None
        while current_node != None:
            if current_node.value == key:
                # If it's not the tail node
                if current_node.next != None:
                    current_node.value = current_node.next.value
                    current_node.next = current_node.next.next
                else:
                    current_node = None
                    # If it's the only node
                    # re initiaize linked list
                    if prev_node == None:
                        self.head = None
                    # break link to the last node
                    else:
                        prev_node.next = None
                return
            prev_node = current_node
            current_node = current_node.next
    
    # delete tail node using node.next.next method
    # Time: O(n) / Space: O(1)
    def deleteNode(self, key) -> None:
        if self.empty():
            return
        current_node = self.head
        if current_node.value == key:
            self.deleteFrontNode()
            return

        while current_node.next != None:
            if current_node.value == key:
                current_node.value = current_node.next.value
                current_node.next = current_node.next.next
                return
            if current_node.next.value == key and current_node.next.next == None:
                current_node.next = None
                return
            current_node = current_node.next
 

    # Time: O(n) / Space: O(1)
    def print(self) -> None:
        print('[',end='')
        current_node = self.head
        while current_node != None:
            print(current_node.value,end=' ')
            current_node = current_node.next
        print(']\n',end='')

def main():
    ll = LinkedList()
    ll.insert(5); ll.insert(2); ll.insert(3); ll.append(7); ll.append(4); ll.append(9)
    ll.print() # [3 2 5 7 4 9 ]
    print(ll.contains(5), ll.contains(8)) # True False
    ll.deleteNodeWithPrev(2)
    ll.deleteNode(7); ll.deleteNode(9)
    ll.deleteNodeWithPrev(4)
    ll.print() # [3 5 ]
    ll.deleteNode(3); ll.deleteNode(5)
    ll.print() # []
    ll.insert(3); ll.append(7)
    ll.print() # [3 7]
    ll.deleteFrontNode(); ll.deleteRearNode()
    ll.print() # []

if __name__ == "__main__":
    main()
