class Node:  # Creating a Node class
    def __init__(self, entry):
        self.entry = entry
        self.next = None


class LinkedList:  # Creating and initializing a Linked List class
    def __init__(self):
        self._front = None
        self._length = 0

    def get_entry(self, index):  # Allows us to get an entry at a specific index
        temp_jumper = self._front
        if 0 <= index < self._length:
            for i in range(index):
                temp_jumper = temp_jumper.next
            return temp_jumper.entry
        else:
            raise RuntimeError('Invalid Index')

    def set_entry(self, index, entry):  # Allows us to set an entry at a specific index
        temp_jumper = self._front
        for i in range(1, index):
            temp_jumper = temp_jumper.next
            temp_jumper.next.entry = entry

    def insert(self, index, entry):  # Allows us to insert a value at an index
        if 0 > index > self._length:
            raise RuntimeError('Invalid Index')
        elif self._front is None:
            new_node = Node(entry)
            self._front = new_node
            self._length += 1
        elif index == 0:
            self._length += 1
            new_node = Node(entry)
            new_node.next = self._front
            self._front = new_node
        else:
            temp_jumper = self._front
            self._length += 1
            new_node = Node(entry)
            for i in range(1, index):
                temp_jumper = temp_jumper.next
            new_node.next = temp_jumper.next
            temp_jumper.next = new_node

    def remove(self, index):  # Allows us to remove a value from an index
        before = self._front
        after = self._front
        if index == 0:
            after = after.next
            return after.entry
        elif 0 < index < self._length:
            for i in range(1, index):
                before = before.next
            target = before.next
            after = target.next
            before.next = after
            return target.entry
        else:
            raise IndexError('Invalid Index')
        self._length -= 1

    def clear(self):  # Clears the entire list
        self._front = None
        self._length = 0

    def len(self):  # Keeps track of the length of the list
        count = 0
        node = self._front
        while node:
            count += 1
            node = node.next
        return count


