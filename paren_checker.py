from atds import Stack

def is_valid(expression):
    stack = Stack()

    legal = True

    for char in list(expression):
        if char == "(":
            stack.push(char)
        if char == ")":
            if stack.peek() == "(":
                stack.pop()
            else:
                legal = False

    if stack.size() != 0:
        legal = False

    return legal

def main():
    pass

if __name__ == "__main__":
    main()
