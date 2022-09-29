#!/usr/bin/env python3

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = self.tail = None

    # Time: O(1) / Space: O(n)
    def append(self, data) -> None:
        if not self.head:
            self.head = self.tail = Node(data)
        else:
            old_tail = self.tail
            self.tail.next = Node(data)
            self.tail = self.tail.next
            self.tail.prev = old_tail

    # Time: O(1) / Space: O(1)
    def insert(self, data) -> None:
        if not self.head:
            self.head = self.tail = Node(data)
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
    
    # Time: O(n) / Space: O(1)
    # Guaranteed half traversal at max time O(n/2)
    def contains(self, key) -> bool:
        curr_forward = self.head
        curr_backwards = self.tail
        # traversal_counter = 0
        while curr_forward != None or curr_backwards != None:
            # traversal_counter += 1
            if curr_forward.value == key or curr_backwards.value == key:
                return True
            if curr_forward == curr_backwards.prev or curr_forward == curr_backwards:
                return False
            curr_forward = curr_forward.next
            curr_backwards = curr_backwards.prev
        return False

    # Time: O(1) / Space: O(1)
    def empty(self) -> bool:
        return self.head == None
    
    # Time: O(1) / Space: O(1)
    def deleteFrontNode(self) -> None:
        if self.empty():
            return
        if self.head.next == None:
            self.head = self.tail =None
        else:
            self.head.next.prev = None
            self.head.value = self.head.next.value
            self.head.next = self.head.next.next

    # Time: O(1) / Space: O(1)
    def deleteRearNode(self) -> None:
        if self.empty():
            return
        if self.tail.prev == None:
            self.tail = self.head =None
        else:
            self.tail.prev.next = None
            self.tail.value = self.tail.prev.value
            self.tail.prev = self.tail.prev.prev
    
    # Time: O(n) / Space: O(1)
    def deleteNodeByKey(self, key) -> None:
        if self.empty():
            return
        current_node = self.head
        if current_node.value == key:
            self.deleteFrontNode()
            return

        while current_node.next != None:
            if current_node.value == key:
                current_node.prev = current_node.next.prev.prev
                current_node.value = current_node.next.value
                current_node.next = current_node.next.next
                return
            if current_node.next.value == key and current_node.next.next == None:
                self.tail = current_node
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

    # Time: O(n) / Space: O(1)
    def reversePrint(self) -> None:
        print('[',end='')
        current_node = self.tail
        while current_node != None:
            print(current_node.value,end=' ')
            current_node = current_node.prev
        print(']\n',end='')

def main():
    dll = DoubleLinkedList()
    dll.append(5); dll.append(3); dll.append(3); dll.append(2); dll.append(33); dll.append(333); dll.append(15)
    dll.insert(11); dll.insert(22)
    print("contains 5: ",dll.contains(5)) # True
    print("contains 3: ",dll.contains(3)) # True
    print("contains 4: ",dll.contains(4)) # False
    dll.print() # [22 11 5 3 3 2 33 333 15 ]
    dll.deleteRearNode(); dll.deleteRearNode(); dll.deleteRearNode(); 
    dll.print() # [22 11 5 3 3 2 ]
    dll.deleteNodeByKey(22); 
    dll.deleteNodeByKey(0); 
    dll.print() # [11 5 3 3 2 ]
    dll.reversePrint() # [2 3 3 5 11 ]

    print("Testing 2nd Double Linked List")
    dll2 = DoubleLinkedList()
    dll2.insert(11); dll2.insert(22); dll2.insert(33)
    dll2.print() # [33 22 11 ]
    dll2.deleteNodeByKey(22); dll2.deleteNodeByKey(11)
    dll2.print() # [33 ]
    dll2.deleteNodeByKey(33)
    dll2.print() # []
    dll2.deleteNodeByKey(24)
    dll2.print() # []

if __name__ == "__main__":
    main()
