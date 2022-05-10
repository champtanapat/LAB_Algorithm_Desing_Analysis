class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

 # Linked List class
class LinkedList:
    
    # Function to initialize the Linked
    # List object
    def __init__(self):
        self.head = None


if __name__=='__main__':
     # Start with the empty list
    llist = LinkedList()
 
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)


    