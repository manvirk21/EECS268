from binarynode import BNode


class BST:
    def __init__(self):  # initiating BST class
        self._root = None

    def search(self, key):
        return self._rec_search(key, self._root)  # using recursive function to search

    def _rec_search(self, key, cur_node):  # creating a recursive function to search the bst
        if cur_node is None:
            raise RuntimeError("SORRY! Item not found")
        if cur_node.entry == key:
            return cur_node.entry
        else:
            if cur_node.entry < key:
                return self._rec_search(key, cur_node.right)
            if cur_node.entry > key:
                return self._rec_search(key, cur_node.left)

    def add(self, entry):  # using recursive function to add
        # check for an empty BST
        if self._root is None:
            self._root = BNode(entry)
        else:
            self._rec_add(entry, self._root)

    def _rec_add(self, entry, cur_node):  # creating a recursive function to add to the bst
        if cur_node.entry > entry:
            if cur_node.left is None:
                cur_node.left = BNode(entry)
            else:
                self._rec_add(entry, cur_node.left)
        elif cur_node.entry < entry:
            if cur_node.right is None:
                cur_node.right = BNode(entry)
            else:
                self._rec_add(entry, cur_node.right)
        else:
            raise RuntimeError('SORRY! No Duplicates Allowed')

    def pre(self, func, cur_node):  # preorder traversal
        if cur_node is not None:
            # Print the data of node
            func(cur_node.entry)
            # Then recursion on left child
            self.pre(func, cur_node.left)
            # Recursion on right child
            self.pre(func, cur_node.right)

    def visit_pre(self, func):
        if self._root is None:
            print("ERROR")
            # Recursion on left child
        else:
            self.pre(func, self._root)

    def post(self, func, cur_node):  # postorder traversal
        if cur_node is not None:
            # Recursion on left child
            self.post(func, cur_node.left)
            # Recursion on right child
            self.post(func, cur_node.right)
            # Print the data of node
            func(cur_node.entry)

    def visit_post(self, func):
        if self._root is None:
            print("ERROR")
        else:
            self.post(func, self._root)

    def in_order(self, func, cur_node):
        if cur_node is not None:
            # Recursion on left child
            self.in_order(func, cur_node.left)
            # Print the data of node
            func(cur_node.entry)
            # Recursion on right child
            self.in_order(func, cur_node.right)

    def visit_in_order(self, func):  # inorder traversal
        if self._root is None:
            print("ERROR")
        else:
            self.in_order(func, self._root)

    def successor(self, cur_node):  # helper function for deleting to find the child
        cur_node = cur_node.left
        while cur_node.right:
            cur_node = cur_node.right
        return cur_node.entry

    def predecessor(self, cur_node):  # helper function for deleting to find the parent
        cur_node = cur_node.right
        while cur_node.left:
            cur_node = cur_node.left
        return cur_node.entry

    def delete(self, entry):  # recursive function for deleting
        return self.deleting(self._root, entry)

    def deleting(self, cur_node, key):  # function to delete the desired entry
        if cur_node is None:
            print("SORRY! Not in tree!")
        if not cur_node:
            return None
        if key > cur_node.entry:
            cur_node.right = self.deleting(cur_node.right, key)
        elif key < cur_node.entry:
            cur_node.left = self.deleting(cur_node.left, key)
        else:
            if not (cur_node.left or cur_node.right):
                cur_node = None
            elif cur_node.left:
                cur_node.entry = self.successor(cur_node)
                cur_node.left = self.deleting(cur_node.left, cur_node.entry)
            else:
                cur_node.entry = self.predecessor(cur_node)
                cur_node.right = self.deleting(cur_node.right, cur_node.entry)
        return cur_node

    def copy(self, node):  # basic copy of the node
        # base case
        if node is not None:
            # create a new node with the same data as the root node
            clone = BNode(node.entry)
            # clone the left and right subtree
            clone.left = self.copy(node.left)
            clone.right = self.copy(node.right)
            # return cloned node
            return clone
        return None

    def clone_tree(self):  # making a new tree to copy and starting the copy process
        #  Create new BinaryTree
        tree = BST()
        #  Get new root
        tree._root = self.copy(self._root)
        #  Returns a new binary tree
        return tree
