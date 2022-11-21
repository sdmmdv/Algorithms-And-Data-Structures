#!/usr/bin/env python3

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    # Time: O(1) / Space: O(1)
    def empty(self) -> bool:
        return self.tail == None
    
    # Time: O(1) / Space: O(1)
    def insert(self, data):
        pass

    def inOrderTraversal(self):
        inOrderList = []
        
        def recurInOrder(node: Node):
            if node == None:
                return
            recurInOrder(node.left)
            inOrderList.append(node.value)
            recurInOrder(node.right)
            
        recurInOrder(self.root)
        return inOrderList 

    def preOrderTraversal(self):
        preOrderList = []
        
        def recurPreOrder(node: Node):
            if node == None:
                return
            preOrderList.append(node.value)
            recurPreOrder(node.left)
            recurPreOrder(node.right)
            
        recurPreOrder(self.root)
        return preOrderList

    def postOrderTraversal(self):
        postOrderList = []
        
        def recurPostOrder(node: Node):
            if node == None:
                return
            recurPostOrder(node.left)
            recurPostOrder(node.right)
            postOrderList.append(node.value)

        recurPostOrder(self.root)
        return postOrderList

def main():
    BT = BinaryTree()
    BT.root = Node(1)
    BT.root.left = Node(2)
    BT.root.right = Node(3)
    BT.root.left.left = Node(4)
    BT.root.left.right = Node(5)

    # # # # # # # # # # # # #
    #         1             #
    #       /   \           #
    #     2       3         #
    #   /   \               #
    # 4       5             #
    #                       #
    # # # # # # # # # # # # #

    print("Pre order Traversal --> ", BT.preOrderTraversal())
    print("In order Traversal --> ", BT.inOrderTraversal())
    print("Post order Traversal --> ", BT.postOrderTraversal())



if __name__ == "__main__":
    main()
