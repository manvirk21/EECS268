"""
Author: Manvir Kaur
KUID: 3064194
Date: 04/29/2022
Lab: lab09
Last modified: 05/03/2022
Purpose: Processing Pokemon Data Using BST
"""


class BNode:
    def __init__(self, entry):  # initializing the BNode class
        self.entry = entry
        self.left = None
        self.right = None
