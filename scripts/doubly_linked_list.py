# This node class will be handled by the Linked List that contains data, a next pointer, and a previous pointer
class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


# A double Linked List that has a head node reference, a tail node reference, and a length
class doubly_linked_list:
    def __init__(self):
        self.head = node()
        self.tail = node()
        self.length = 0

    # Appending creates a new node that is added to the end of the Linked List
    def append(self, data):
        new_node = node(data)

        if self.length == 0:
            self.head = new_node
            self.tail = self.head
        else:
            # Add the new node to the end of the tail
            new_node.prev = self.tail
            self.tail.next = new_node
            # Set new node as new tail and add length
            self.tail = new_node
        self.length += 1
        return print("%s was added to Linked List. Length is now %d" % (str(data), self.length))

    # For each node in the Linked List, collect the data in order and print the list
    def display(self):
        if self.length == 0:
            return None
        cur = self.head
        elems = []
        while cur != None:
            elems.append(cur.data)
            cur = cur.next
        return print(elems)

    # Display the Linked list in reverse order
    def display_reverse(self):
        if self.length == 0:
            return None
        cur = self.tail
        elems = []
        while cur != None:
            elems.append(cur.data)
            cur = cur.prev
        return print(elems)

    # Return the data for the node at given index in Linked List
    def get(self, index):
        # 0 =< index < length
        if index >= self.length or index < 0:
            print("ERROR: Index out of range!")
            return None
        # Start at head node and iterate through Linked List
        cur = self.head
        cur_idx = 0
        # As long as there is a next node, iterate and check if the next node is the ask
        while cur != None:
            if cur_idx == index:
                print(cur.data)
                return cur
            cur_idx += 1
            cur = cur.next

    # Remove a node from the Linked List at the given index
    def erase(self, index):
        if index >= self.length or index < 0:
            print("ERROR: Index out of range!")
            return None

        cur = self.get(index)

        # If only one node in list aka length = 1
        if self.head == cur and self.tail == cur:
            self.head = node()
            self.tail = node()
        else:
            # If we're at the tail
            if cur.next == None:
                self.tail = cur.prev
                self.tail.next = None

            # If we're at the head
            elif cur.prev == None:
                self.head = cur.next
                self.head.prev = None

            # Otherwise normal conditions
            else:
                cur.prev.next = cur.next
        self.length -= 1
        return
