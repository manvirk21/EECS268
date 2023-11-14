"""
Author: Manvir Kaur
KUID: 3064194
Date: 04/22/2022
Lab: lab08
Last modified: 04/29/2022
Purpose: Processing Pokemon Data Using BST
"""


class BNode:
    def __init__(self, entry):  # initializing the BNode class
        self.entry = entry
        self.left = None
        self.right = None
