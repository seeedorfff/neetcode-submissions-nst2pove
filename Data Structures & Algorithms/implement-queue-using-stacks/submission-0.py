class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        # always push to stack1
        self.stack1.append(x)

    # it's a queue, if elements are still in stack2,
    # they need to be addressed before any other that is pushed
    # can only empty into stack2 if it's empty
    def simulate(self) -> None:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

    def pop(self) -> int:
        self.simulate()
        return self.stack2.pop()

    def peek(self) -> int:
        # same here
        self.simulate()
        return self.stack2[-1]

    def empty(self) -> bool:
        # both must be empty
        return max(len(self.stack1), len(self.stack2)) == 0

        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()