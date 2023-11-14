from node import Node

def main():
    front = None
    temp = None
    
    front = Node(55)
    temp = Node(13)
    front.next = temp
    temp.next = Node(42)
    #Create a sequence of Nodes without making any more variables
