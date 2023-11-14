from node import Node

class LinkedList:
    def __init__(self):
        self._front = None
        self._length = 0

    def get_entry(self, index):
        temp_jumper = self._front
        if 0 <= index < self._length:
            for i in range(index):
                temp_jumper = temp_jumper.next
            return temp_jumper.entry
        else:
            raise RuntimeError('Invalid Index')

    def insert(self, index, entry):
        if index == 0:
            self._length += 1
            new_node = Node(entry)
            new_node.next = self._front
            self._front = new_node
        elif index == self._length:
            self._length += 1
            new_node = Node(entry)
            for i in range(index):
                temp_jumper = temp_jumper.next
            temp_jumper.next = new_node
        elif 0 > index > self._length:
            raise RuntimeError('Invalid Index')
        else:
            self._length += 1
            new_node = Node(entry)
            for i in range(index - 1):
                temp_jumper = temp_jumper.next
                temp_jumper.next = new_node

    def remove(self, index):
        before = self._front
        after = self._front
        if index == 0:
            after = after.next
            return after.entry
        elif index > 0 and index < self._length:
            for i in range(index - 1):
                before = before.next
            target = before.next
            after = target.next
            before.next = after
            return target.entry
        else:
            raise IndexError('Invalid Index')
        self._length -= 1

    def clear(self):
        self._front = None
        self._length = 0
