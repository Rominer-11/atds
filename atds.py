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

class Node():
    def __init__(self, data):
        """
        Initializes the node class
        """
        self.data = data
        self.pointer = None

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

    def __repr__(self):
        """
        String representation of node
        """
        return "Node[data=" + str(self.data) + ",next=" + str(self.pointer) + "]"

class UnorderedList():
    def __init__(self):
        """
        Initializes the unordered list
        """
        self.head = None
    
    def add(self, item):
        """
        Adds an item to the unordered list
        """
        new_node = Node(item)
        new_node.set_next(self.head)
        self.head = new_node
        
    def length(self):
        """
        Returns the length of the list
        """
        node_count = 0
        current = self.head
        while current != None:
            node_count += 1
            current = current.get_next()
        return node_count

    def is_empty(self):
        """
        Returns whether or not the list is empty
        """
        return self.head == None

    def remove(self, item):
        """
        Removes an item from the list
        """
        previous = None
        current = self.head

        while current != None:
            if current.get_data() == item:
                if previous == None:
                    self.head = current.get_next()
                    current = current.get_next()
                else:
                    previous.set_next(current.get_next())
                    current = current.get_next()
            else:
                previous = current
                current = current.get_next()

    def __repr__(self):
        """
        Function written by Mr. White

        Creates a representation of the list suitable for printing,
        debugging.
        """
        result = "UnorderedList["
        next_node = self.head
        while next_node != None:
            result += str(next_node.get_data()) + ","
            next_node = next_node.get_next()
        if result[-1] == ",":
        result = result[:-1] # remove trailing comma
        result = result + "]"
        return result

def main():
    pass

if __name__ == "__main__":
    main()
