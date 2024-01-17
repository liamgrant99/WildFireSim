class Node:
    def __init__(self, v, p, n) -> None:
        self.value = v
        self.previous = p
        self.next = n

    def __str__(self) -> str:
        return str(self.value)
    
class DoublyLinkedList:
    def __init__(self) -> None:
        self.size = 0
        self.header = Node(None, None, None)
        self.trailer = Node(None, self.header, None)
        self.header.next = self.trailer

    #Adding underscores infront of method "mangles" the name, which means you cannot use the method directly.
    def add_between(self, n1, n2, v):
        if n1 is None or n2 is None:
            raise ValueError("Nodes Cannot be None")
        if n1.next is not n2:
            raise ValueError("Node2 must follow Node1")

        #Make a new node
        new_node = Node(v, n1, n2)

        #Set n1 next reference to the new node
        n1.next = new_node
        #Set n2 previous reference to the new node
        n2.previous = new_node

        self.size += 1

    def add_first(self, v):
        self.add_between(self.header, self.header.next, v)

    def add_last(self, v):
        self.add_between(self.trailer.previous, self.trailer, v)

    def __str__(self) -> str:
        if self.header.next is self.trailer:
            return "[]"
        reference = self.header
        return_str = "["
        while reference.next.next is not None:
            reference = reference.next
            return_str += str(reference.value) + " "
        
        return return_str.rstrip() + "]"

    def remove_between(self, n1, n2):
        if (n1 is None or n2 is None): # and (n1 is not self.header and n2 is not self.trailer)
            raise ValueError("Nodes Cannot be None")
        if n1.next.next is not n2:
            raise ValueError("Node for removal must be between Node2 and Node1")
        
        return_val = n1.next.value
        n1.next = n2
        n2.previous = n1

        self.size -= 1

        return return_val
    
    def remove_first(self):
        self.remove_between(self.header, self.header.next.next)
    
    def remove_last(self):
        self.remove_between(self.trailer.previous.previous, self.trailer)

    def search(self, value):
        reference = self.header
        reference = reference.next
        count = 0

        while reference.value != value and reference.next.next is not None:
            reference = reference.next
            count += 1
        if reference.value == value:
            return count
        else:
            return -1




