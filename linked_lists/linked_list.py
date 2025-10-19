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
    
    def remove_end(self, data_removed=None):
        if self.head is None:
            return None
        if self.head.next is None:
            data_removed = self.head.data
            self.head = None
            self.tail = None
            return data_removed
        current = self.head
        while current.next.next:
            current = current.next
        data_removed = current.next.data
        current.next = None
        self.tail = current
        return data_removed
    
    def remove_at(self, data):
        if self.head is None:
            return None
        if self.head.data == data:
            return self.remove_beginning()
        current = self.head
        while current.next:
            if current.next.data == data:
                data_removed = current.next.data
                current.next = current.next.next
                if current.next is None:
                    self.tail = current
                return data_removed
        current = current.next
        return None

    def display(self, data_removed=None):
        if removed_beginning is not None:
            print(f"Removed Beginning: {removed_beginning}")
        if removed_end is not None:
            print(f"Removed End: {removed_end}")
        if removed_data is not None:
            print(f"remaining item: {removed_data}")

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
removed_end = sushi_preparation.remove_end()
removed_data = sushi_preparation.remove_at("prepare")
sushi_preparation.display()

