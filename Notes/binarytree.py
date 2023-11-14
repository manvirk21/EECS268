from binarynode import BNode

class BinaryTree:
    def __init__(self):
        self._root = None

    def add(self, entry):
        #assume this works
        #we'll define a formal add when we get to BST

    def search(self, target):
        return self._rec_search(target, self._root)

    def _rec_search(self, target, cur_node):
        if cur_node is None:
            return False
        else:
            if cur_node_entry == target:
                return True
            if cur_node.entry != target:
                return self._rec_search(target, cur_node.left.entry)
            if cur_node.entry != target:
                return self._rec_search(target, cur_node.right.entry)

    def count(self, target):
        return self._rec_count(target, self._root)

    def _rec_count(self, target, cur_node):
        if cur_node == None:
            return 0
        else:
            lst_count = self._rec_count(target, cur_node.left)
            rst_count = self._rec_count(target, cur_node.right)
            if cur_node.entry == target:
                return 1 + lst_count + rst_count
            else:
                return lst_count + rst_count

    def leaf_count(self):
        return self._rec_leaf_count(self._root)

    def _rec_leaf_count(self, cur_node):
        if cur_node is None:
            return 0
        else:
            lst_count = self._rec_leaf_count(cur_node.left)
            rst_count = self._rec_leaf_count(cur_node.right)
            if cur_node.left is None and cur_node.right is None:
                return 1
            else:
                return lst_count + rst_count
