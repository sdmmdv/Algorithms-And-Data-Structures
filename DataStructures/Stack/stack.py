#!/usr/bin/env python3
class Stack:
    # Time: O(1) / Space: O(1) """
    def __init__(self):
        self.elements = []

    # Time: O(1) / Space: O(1) """
    def push(self, data):
        self.elements.append(data)

    # Time: O(1) / Space: O(1) """
    def pop(self):
        if not self.elements:
            return None
        return self.elements.pop()
        # tmp = self.elements[-1]
        # del self.elements[-1] 
        # return tmp

    # Time: O(1) / Space: O(1)
    def top(self):
        return self.elements[-1]

    # Time: O(1) / Space: O(1)
    def size(self):
        return len(self.elements)

    # Time: O(1) / Space: O(1)
    def empty(self):
        return False if self.size() else True

    # Originally printing the whole Stack is not supported
    # Time: O(n) / Space: O(n)
    def print(self):
        tmp_stack = Stack()
        while not self.empty():
            elem = self.pop()
            print(elem, end=' ')
            tmp_stack.push(elem)
        while not tmp_stack.empty():
            self.push(tmp_stack.pop())
        print()


    # Originally Stack doesn't support searching
    # Time: O(n) / Space: O(n)
    def contains(self, data):
        tmp_stack = Stack()
        doesContain = False
        while not self.empty() and not doesContain:
            comp_elem  = self.top()
            if comp_elem == data:
                doesContain = True
            else:
                tmp_stack.push(self.pop())
        while not tmp_stack.empty():
            self.push(tmp_stack.pop())
        return doesContain

def main():
    stack = Stack()
    stack.push(1)
    stack.push(4)
    stack.push(9)
    stack.print()
    print(stack.contains(1))
    print(stack.contains(3))
    print(stack.contains(9))
    stack.pop()
    stack.print()
    stack.pop()
    stack.print()

    stack1 = Stack()

if __name__ == "__main__":
    main()
