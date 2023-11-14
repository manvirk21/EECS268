from node import Node

class Queue:
    def __init__(self):
        self._front = None
        self._back = None

    def enqueue(self, entry):
        if self.is_empty():
            self._front = Node(entry)
            self._back = self._front
        else:
            new_back = Node(entry)
            self._back.next = new_back
            self._back = new_back

    def dequeue(self):  
        if self._front is not None:
            entry = self._front.entry
            self._front = self._front.next
            return entry
        else:
            raise RuntimeError('Queue empty')

    def peek_front(self):  
        if self._front is not None:
            return self._front

    def is_empty(self):  
        return self._front is None
