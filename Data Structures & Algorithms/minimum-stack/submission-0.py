class MinStack:

    def __init__(self):
        self.stack: list = []
        self.Minstack: list = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.Minstack[-1] if self.Minstack else val)
        self.Minstack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.Minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)
