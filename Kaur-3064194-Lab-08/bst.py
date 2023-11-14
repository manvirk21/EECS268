from binarynode import BNode


class BST:
    def __init__(self):
        self._root = None

    def search(self, key):
        return self._rec_search(key, self._root)  # using recursive function to search

    def _rec_search(self, key, cur_node):  # creating a recursive function to search the bst
        if cur_node is None:
            raise RuntimeError("Item not found")
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
            raise RuntimeError('No Duplicates Allowed')

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
