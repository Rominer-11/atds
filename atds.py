"""
atds.py

Includes the following classes
    - Stack
    - Queue
    - Deque
    - Node
    - Unordered list
    - Vertex
    - Graph

"""

__author__ = "August Cho"
__version__ = "2026-03-19"

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
    
    def append(self, item):
        """
        Appends an item to the end of the list
        """
        current = self.head
        previous = None
        
        while current.get_next() != None:
            previous = current
            current = current.get_next()

        current.set_next(Node(item))

    def index(self, item):
        """
        Finds the index of a given item
        """
        current = self.head
        index = 0
        foundIndex = 0
        found = False
        while current != None and found == False:
            if current.get_data() == item:
                foundIndex = index
                found = True
            else:
                current = current.get_next()
                index += 1

        return foundIndex

    def insert(self, pos, item):
        """
        Inserts an item at a given position
        """
        current = self.head
        previous = None
        index = 0
        loop = True

        while loop:
            if index == pos:
                newNode = Node(item)
                if previous != None:
                    previous.set_next(newNode)
                if index == 0:
                    self.head = newNode
                newNode.set_next(current)
                loop = False
            else:
                previous = current
                current = current.get_next()
               
                index += 1

    def pop(self, pos = None):
        """
        Pops item at position
        """
        if pos == None:
            pos = self.length() - 1
        
        current = self.head
        previous = None
        index = 0
        returnVal = None
        loop = True
        while loop:
            if index == pos:
                returnVal = current
                if index == 0:
                    self.head = current.get_next()
                else:
                    if current != None:
                        previous.set_next(current.get_next())
                loop = False
            else:
                previous = current
                current = current.get_next()
                index += 1

        return returnVal

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

    def search(self, item):
        """
        Searches for a given item in the list
        """
        found = False
        current = self.head
        while current != None and found == False:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def __repr__(self):
        """Creates a representation of the list suitable for printing,
        debugging.
        """
        result = "UnorderedList["
        next_node = self.head
        while next_node != None:
            result += str(next_node.get_data()) + ","
            next_node = next_node.get_next()
        result = result + "]"
        return result

class LinearSearcher():
    def __init__(self):
        pass

    def search(self, array, target):
        targetIndex = None
        index = 0
        while index < len(array) and targetIndex == None:
            if target == array[index]:
                targetIndex = index
            index += 1
        return targetIndex

class BinarySearcher():
    def __init__(self):
        pass

    def search(self, array, target):
        targetIndex = None
        upperBound = len(array)
        lowerBound = 0
        middleIndex = 1
        
        while upperBound > lowerBound and middleIndex != targetIndex and targetIndex == None:
            middleIndex = lowerBound + ((upperBound - lowerBound) // 2)
            
            if array[middleIndex] == target:
                targetIndex = middleIndex
            elif array[middleIndex] < target:
                lowerBound = middleIndex
            elif array[middleIndex] > target:
                upperBound = middleIndex

        if middleIndex == targetIndex:
            if target == array[middleIndex]:
                targetIndex = middleIndex
            elif target == array[middleIndex + 1]:
                targetIndex = middleIndex + 1

        return targetIndex

class HashTable():
    """
    Hash table class! (Awesome)
    """

    def __init__(self, size):
        self.size = size
        self.slots = []
        self.data = []
        self.length = 0
        for i in range(size):
            self.slots.append([])
            self.data.append([])

    def hash_function(self, key):
        return key % self.size

    def put(self, key, value):
        index = self.hash_function(key)
        self.slots[index].append(key)
        self.data[index].append(value)

        self.length += 1

    def get(self, key):
        index = self.hash_function(key)
        returnValue = None
        for i in range(len(self.slots[index])):
            if self.slots[index][i] == key:
                returnValue = self.data[index][i]

        return returnValue

    def __len__(self):
        return self.length

    def __repr__(self):
        return "Keys: " + str(self.slots) + "\n" + "Values: " + str(self.data)

    def __str__(self):
        return self.__repr__()


class Vertex(object):
    """Improves the vertex class to include not only a key and neighbors,
    but also a "color" (used to identify exploration state), a "distance"
    (used by some algorithms to measure number of vertices traversed), and
    "previous", a convenient pointer to a previous vertex in a path.
    Note also that the "weight" to a neighbor is coded as a value in a
    key-value pair in the `neighbors` dictionary.
    """
    def __init__(self, key):
        """Constructs a vertex with a key value and an empty dictionary 
        in which we'll store other vertices to which this vertex is connected.
        """
        self.key = key
        self.neighbors = {}   # empty dictionary for neighboring vertices
        self.color = 'white'
        self.distance = 0
        self.previous = None
    
    def set_neighbor(self, other, weight=0):
        """Adds a reference to a neighboring Vertex object to the dictionary, 
        to which this vertex is connected by an edge. If a weight is not indicated, 
        default weight is 0.
        """
        self.neighbors[other] = weight
    
    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color
    
    def get_distance(self):
        return self.distance
    
    def set_distance(self, new_distance):
        self.distance = new_distance
    
    def get_previous(self):
        return self.previous
    
    def set_previous(self, new_prev):
        self.previous = new_prev
    
    def __repr__(self):
        """Returns a representation of the vertex and its neighbors, suitable for 
        printing. Check out the example of 'list comprehension' here!
        """
        return f"Vertex({self.key}"
        
    def __str__(self):
        return ( f"{self.key} connected to: "
        + f"{[x.key for x in self.neighbors]}")
    
    def get_neighbors(self):
        return self.neighbors.keys()
    
    def get_key(self):
        return self.key
    
    def get_neighbor(self, other):
        """Returns the weight of an edge connecting this vertex with another,
        or None if the neighbor doesn't exist
        """
        return self.neighbors.get(other, None)

class Graph(object):
    """Describes the Graph class, which is primarily a dictionary
    mapping vertex names to Vertex objects, along with a few methods
    that can be used to manipulate them.
    """
    def __init__(self):
        self.vertices = {}

    def set_vertex(self, key):
        self.vertices[key] = Vertex(key)

    def get_vertex(self, key):
        """Looks for the key in the dictionary of Vertex objects, and
        returns the Vertex if found. Otherwise, returns None.
        """
        '''
        # This is the classic way of doing that
        if key in self.graph.keys():
            return self.graph[key]
        else:
            return None
        '''
        # Single-line alternative
        return self.vertices.get(key, None)

    def __contains__(self, key):
        """This 'dunder' expression is written so we can use Python's "in"
        operation: If the parameter 'key' is in the dictionary of vertices,
        the value of "key in my_graph" will be True, otherwise False.
        """
        return key in self.vertices

    def add_edge(self, from_vert, to_vert, weight=0):
        """Adds an edge connecting two vertices (specified by key
        parameters) by modifying those vertex objects. Note that
        the weight can be specified as well, but if one isn't
        specified, the value of weight will be the default value
        of 0.
        """
        # if the from_key doesn't yet have a vertex, create it
        if from_vert not in self.vertices:
            self.set_vertex(from_vert)
        # if the to_key doesn't yet have a vertex, create it
        if to_vert not in self.vertices:
            self.set_vertex(to_vert)
        # now we can create the edge between the two
        self.vertices[from_vert].set_neighbor(self.vertices[to_vert], weight)

    def get_vertices(self):
        return self.vertices.keys()

    def __iter__(self):
        """Another 'dunder' expression that allows us to iterate through
        the list of vertices.
        Example use:
        for vertex in graph:  # Python understands this now!
            print(vertex)
        """
        return iter(self.vertices.values())

def main():
    pass

if __name__ == "__main__":
    main()
