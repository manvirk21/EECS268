#bst.py

from bnode import BNode


class BST:
    def __init__(self):
        self._root = None

    #Assume an add works

    def search(self, key):
        return self._rec_search(self, key, cur_node)

    def _rec_search(self, key, cur_node):
        #Assume that comparison operators are overloaded
        #Example:   cur_node.entry == key    is valid
        #cur_node < key and cur_node > key is also valid
        if cur_node is None:
            raise RuntimeError
        if cur_node.entry == key:
            return cur_node.entry
        else:
            if cur_node.entry > key:
                self._rec_search(key, cur_node.right)
            if cur_node.entry < key:
                self._rec_search(key, cur_node.left)

    def add(self, entry):
        #check for an empty BST
        if self._root == None:
            self._root = BNode(entry)
        elif self._root.entry < entry:
            #more in this step
            self._rec_add(entry, self._root.right)
        elif self._root.entry > entry:
            #more in this step
            self._rec_add(entry, self._root.left)
        else:
            raise RuntimeError('No Duplicates Allowed')

    def _rec_add(self, entry, cur_node):
        if cur_node.entry > entry:
            if cur_node.left == None:
                cur_node.left = BNode(entry)
            else:
                self._rec_add(entry, cur_node.left)
        elif cur_node.entry < entry:
            if cur_node.right == None:
                cur_node.right = BNode(entry)
            else:
                self._rec_add(entry, cur_node.right)
         else:
             raise RuntimeError('No Duplicates Allowed')

