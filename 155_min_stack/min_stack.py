class Node:
    def __init__(self, val):
        self.value = val
        self.local_min = None


class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        node = Node(val)
        prev_min = self.stack[-1].local_min if (len(self.stack) > 0 and self.stack[-1].local_min is not None) else val
        node.local_min = min(val, prev_min)
        self.stack.append(node)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1].value

    def getMin(self) -> int:
        return self.stack[-1].local_min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
def fail_one():
    # ["MinStack","push","push","push","getMin","pop","getMin"]
    correct = [None, None, None, None, 0, None, 0]
    r = []
    stack = MinStack()
    r.append(stack.push(0))
    r.append(stack.push(1))
    r.append(stack.push(0))
    r.append(stack.getMin())
    r.append(stack.pop())
    r.append(stack.getMin())
    print(f"{correct}")
    print(f"{r}")


def main():
    fail_one()


main()
