class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.tail = new_node
            self.head = new_node
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
    def remove_beginning(self):
        data_removed = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return data_removed
    def remove_end(self):
        data_removed = self.
    
    def display(self, data_removed=None):
        if data_removed is not None:
            print(f"removed: {data_removed}")
        current_data = self.head
        while current_data:
            print(current_data.data, end=">")
            current_data = current_data.next
        print("nonee")
   
sushi_preparation = LinkedList()
sushi_preparation.insert_at_end("prepare")
sushi_preparation.insert_at_end("roll")
sushi_preparation.insert_at_beginning("assemble")
removed_beginning = sushi_preparation.remove_beginning()
sushi_preparation.display(removed_beginning)
