#Doing singly linked lists
class Node:
    def __init__(self, v, n) -> None:
        self.value = v
        self.next = n #The next node 
    
    def __str__(self) -> str:
        return f"{self.value}"
    
class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def get_size(self):
        return self.size

    def is_empty(self):
        if self.size == 0:
            return True
        return False

    def add_first(self, v): #Add a new value to the head of the list
        #Step 1: create new node
        new_node = Node(v, self.head)
        #Step 2: change head reference point to new node.
        self.head = new_node
        #Step 3: Increment size
        self.size += 1

    def remove(self): #Remove head value if list is not empty. Returned removed value, return value error if empty.
        #Step 1: Check if list is empty
        if self.size > 0:
            #Step 2: Remember value
            value_to_return = self.head.value
            #Advance head and change size. 
            self.head = self.head.next
            self.size -=1
            return value_to_return
        else:
            #Step 3: If list is empty, raise value error
            raise ValueError("List is Empty")
            #is operator compares REFERENCES
        
    def remove_first(self):
        if self.size == 0:
            raise ValueError("List is empty")
        return_val = self.head.value
        self.head = self.head.next
        self.size -= 1
        return return_val

    def __str__(self) -> str:
        result = "["
        reference = self.head
        while not reference is None:
            result += str(reference) + " "
            reference = reference.next
        
        return result.rstrip() + "]"
    
    def find_minimum(self):
        minimum = self.head.value 
        reference = self.head
        while reference is not None:
            if reference.value < minimum:
                minimum = reference.value
            reference = reference.next
        return minimum 
    
    def remove_last(self):
        if self.is_empty():
            raise ValueError("List is empty.")
        else:
            return_val = None
            if self.size == 1:
                return_val = self.head.value
                self.head = None
                self.size -= 1
                return return_val
            else:
                reference = self.head
                while reference.next.next is not None:
                    reference = reference.next
                return_val = reference.next.value
                reference.next = None
                self.size -= 1
                return return_val

    def get(self, index):
        count = 0
        reference = self.head
        while count != index:
            reference = reference.next
            count += 1
        return reference.value
    
    def add_last(self, v):
        new_node = Node(v, None)
        reference = self.head
        while reference.next is not None:
            reference = reference.next
        reference.next = new_node
        self.size += 1
    
    def remove_at_index(self, index):
        if index > self.size - 1 or index < 0:
            raise IndexError("Index not within range of list.")
        elif index == 0:
            self.head = None
            self.size -= 1
        else:
            count = 0
            reference = self.head
            while count+1 != index:
                reference = reference.next
                count += 1
            reference.next = reference.next.next
            self.size -= 1

    def rotate(self, index):
        if index < 0 or index > self.size -1:
            raise IndexError("Index out of bounds.")
        else:
            reference = self.head
            while reference.next is not None:
                reference = reference.next

            for i in range(index):
                temp = self.head
                reference.next = temp
                self.head = temp.next
                temp.next = None

                reference = reference.next
