from SLL import SinglyLinkedList

#Do not inherit singly linked list, because if top is at head, remove last would allow to remove head?
class Stack:
    def __init__(self) -> None:
        self.the_stack = SinglyLinkedList()

    def push(self, v):
        self.the_stack.add_first(v)
    
    def pop(self):
        v = self.the_stack.remove_first()
        return v
        #Need to return last (LIFO) last in first out

    def top(self):
        return self.the_stack.head.value

    def is_empty(self):
        return self.the_stack.size == 0

    def get_size(self):
        return self.the_stack.size