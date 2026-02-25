"""
atds.py

Includes the follwing classes
    - Stack
    - Queue
    - Deque

"""

__author__ = "August Cho"
__version__ = "2026-02-17"

class Stack():
    def __init__(self):
        """
        Create empty stack
        """
        self.stack = []

    def push(self, item):
        """
        Push item to stack
        """
        self.stack.append(item)

    def peek(self):
        """
        Peek at top of stack
        """
        if len(self.stack) > 0:
            return self.stack[-1]

    def pop(self):
        """
        Pop item at top of stack
        """
        if len(self.stack) > 0:
            return self.stack.pop() 

    def size(self):
        """
        Return size of stack
        """
        return len(self.stack)

    def is_empty(self):
        """
        Checks if stack is empty
        """
        return self.size() == 0
    
    def __repr__(self):
        """
        Returns string representation of stack
        """
        return str(self.stack)

class Queue():
    def __init__(self):
        """
        Create empty queue
        """
        self.queue = []

    def enqueue(self, item):
        """
        Places item in queue
        """
        self.queue = [item] + self.queue

    def dequeue(self):
        """
        Removes and returns first item in queue
        """
        if len(self.queue) > 0:
            return self.queue.pop()

    def peek(self):
        """
        Returns first item in queue
        """
        if len(self.queue) > 0:
            return self.queue[-1]

    def size(self):
        """
        Returns size of queue
        """
        return len(self.queue)

    def is_empty(self):
        """
        Checks if queue is empty
        """
        return self.size() == 0

    def __repr__(self):
        """
        Returns string representation of queue
        """
        return str(self.queue)

class Deque():
    def __init__(self):
        """
        Initializes deque class
        """
        self.deque = []

    def add_front(self, item):
        """
        Adds an item to the front of the deque
        """
        self.deque.append(item)

    def add_rear(self, item):
        """
        Adds an item to the end of the deque
        """
        self.deque = [item] + self.deque

    def remove_front(self):
        """
        Removes and returns the front of the deque
        """
        if len(self.deque) > 0:
            return self.deque.pop()

    def remove_rear(self):
        """
        Removes and returns the end of the deque
        """
        if len(self.deque) > 0:
            item = self.deque[0]
            self.deque = self.deque[0:-1]
            return item 

    def size(self):
        """
        Returns size of deque
        """
        return len(self.deque)

    def is_empty(self):
        """
        Returns whether or not deque is empty
        """
        return self.size() == 0

    def __repr__(self):
        """
        Returns string representation of deque
        """
        return str(self.deque)

class Node(data, pointer):
    def __init__(self):
        """
        Initializes the node class
        """
        self.data = data
        self.pointer = pointer

    def get_data(self):
        """
        Returns the data of the nade
        """
        return self.data

    def get_next(self):
        """
        Returns the pointer of the node
        """
        return self.pointer

    def set_data(self, data):
        """
        Sets the data of the node
        """
        self.data = data

    def set_next(self, pointer):
        """
        Sets the pointer of the node
        """
        self.pointer = pointer

def main():
    pass

if __name__ == "__main__":
    main()
