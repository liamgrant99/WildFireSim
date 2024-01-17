from DLL import DoublyLinkedList
"""
Queue class
"""
class Queue:
    def __init__(self) -> None:
        self.the_queque = DoublyLinkedList()

    def enqueque(self, v):
        self.the_queque.add_last(v)

    def dequeque(self):
        v = self.the_queque.header.next.value
        self.the_queque.remove_first()
        return v

    def first(self):
        return self.the_queque.header.next.value
    
    def get_size(self):
        return self.the_queque.size
    
    def is_empty(self):
        return self.the_queque.size == 0
    