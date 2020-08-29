class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):

        # Set current node to head and previous node to None
        current_node = self.head
        prev_node = None

        # Iterate through linked list, while current node does not equal none
        while  current_node != None:

            # Store next node
            next_node = current_node.get_next()

            # Set thenext of current node to previous node
            current_node.set_next(prev_node)

            # Set previous node to current node
            prev_node = current_node

            # Set current node to next node
            current_node = next_node

        # While current node does equal none set head to previous node
        self.head = prev_node
