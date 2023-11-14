"""
Author: Manvir Kaur
KUID: 3064194
Date: 02/25/2022
Lab: lab04
Last modified: 03/04/2022
Purpose: Creating a mock CPU scheduler
"""


class Node:  # Creating a Node class
    def __init__(self, entry):
        self.entry = entry
        self.next = None


class Stack:  # Creating a Stack class
    def __init__(self):
        self._top = None

    def is_empty(self):  # Checks if stack is empty
        return self._top is None

    def push(self, entry):  # Adds to the top of the stack
        temp = self._top
        self._top = Node(entry)
        self._top.next = temp

    def pop(self):  # Removes the top entry in the stack
        if not self.is_empty():
            temp = self._top
            self._top = self._top.next
            return temp.entry
        else:
            raise RuntimeError('Stack Empty')

    def peek(self):  # returns what is at the top of the stack
        if self._top is not None:
            return self._top.entry
        else:
            raise RuntimeError('Stack empty')


class Queue:  # Creating a Queue class
    def __init__(self):
        self._front = None
        self._back = None

    def enqueue(self, entry):  # Adding to the back of the queue
        temp = Node(entry)
        if self._front is None:
            self._front = temp
            self._back = self._front
        else:
            self._back.next = temp
            self._back = temp

    def dequeue(self):  # Removing from the front of the queue
        if self._front is not None:
            entry = self._front.entry
            self._front = self._front.next
            return entry
        else:
            raise RuntimeError('Queue empty')

    def peek_front(self):  # Returns what's at the front of the queue
        if self._front is not None:
            return self._front

    def is_empty(self):  # Checks if queue is empty
        return self._front is None
