from node import Node

class Stack:
    def __init__(self):
        self._top = None

    def is_empty(self):
        return self._top == None

    def push(self, entry):
        temp = self._top
        self._top = Node(entry)
        self._top.next = temp

    def pop(self):
        if self._top != None:
            temp = self._top #don't need this
            self._top = self._top.next
        else:
            raise RuntimeError('Stack empty')

    def peek(self):
        if self._top != None:
            return self._top.entry
        else:
            raise RuntimeError('Stack empty')
