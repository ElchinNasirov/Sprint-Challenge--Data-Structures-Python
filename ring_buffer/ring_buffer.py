from doubly_linked_list import DoublyLinkedList 

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head

        elif self.storage.length == self.capacity:
            remove_head = self.storage.head
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)

            if remove_head == self.current:
                self.current = self.storage.tail

    def get(self):
        list_buffer_contents = []

        start = self.current
        list_buffer_contents.append(start.value)

        if start.next:
            next_item = start.next
        else:
            next_item = self.storage.head

        while next_item != start:
            list_buffer_contents.append(next_item.value)

            if next_item.next:
                next_item = next_item.next
            else:
                next_item = self.storage.head
        return list_buffer_contents