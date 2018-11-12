class MyStack:
    def __init__(self):
        self._asd = []

    def push(self, item):
        self._asd.top(item)

    def pop(self):
        return self._asd.pop()

    def isEmpty(self):
        return len(self._asd) == 0

def main():
    stack = MyStack()
    stack.push('a')
    stack.push(b'')
    stack.push('c')
    stack.pop()
    print(stack)
    if stack:
        print("Stack is not empty")
    stack.pop()
    stack.pop()
    if stack.isEmpty():
        print("Stack is empty")



if __name__ == '__main__':
    main()
