# data structure definition


class Stack:

    def __init__(self):
        self.s = []

    def push(self, item):
        self.s.append(item)

    def pop(self):
        return self.s.pop()

    def is_empty(self):
        return not self.s

    def get_length(self):
        return len(self.s)

    def __str__(self):
        return str(self.s)


if __name__ == "__main__":
    # test sequence
    my_stack = Stack()
    assert my_stack.is_empty()
    assert my_stack.get_length() == 0
    my_stack.push(4)
    assert not my_stack.is_empty()
    assert my_stack.get_length() == 1
    my_stack.push(-1)
    assert my_stack.get_length() == 2
    num = my_stack.pop()
    assert num == -1
    num = my_stack.pop()
    assert my_stack.is_empty()
