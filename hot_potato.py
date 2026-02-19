from atds import Queue

"""
Hot potato
"""

__author__ = "August Cho"
__version__ = "2026-02-17"

def main():
    queue = Queue()
    people = ["Lissa", "Iris", "Evan", "Jamie", "August", "Ethan the jet"]

    for person in people:
        queue.enqueue(person)
   
    print("Original queue: " + str(queue))     

    while queue.size() > 1: 

        number = 6

        for i in range(number - 1):
            person = queue.dequeue()
            print(person + " has the potato")
            queue.enqueue(person)

        person = queue.dequeue()
        print(person + " blew up")

    person = queue.peek()
    print(person + " wins")

if __name__ == "__main__":
    main()
