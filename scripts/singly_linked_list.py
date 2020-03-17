# This node class will be handled by the Linked List that contains data and a next pointer.
class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class singly_linked_list:
    def __init__(self):
        # Head node is created that stores no data but signals start of the singly LL
        self.head = node()
        self.length = 0

    def append(self, data):
        # Create new node
        new_node = node(data)

        # If list is empty, set node as the head
        if self.length == 0:
            self.head = new_node
        else:
            cur = self.head
            # Get to last node in list
            while cur.next != None:
                cur = cur.next
            cur.next = new_node
        self.length += 1

    def display(self):
        # Store data of each node in order
        elems = []
        # Start at head
        cur = self.head
        # Iterate through LL
        while cur != None:
            elems.append(cur.data)
            cur = cur.next
        return print(elems)

    def get(self, index):
        # Check that index isnt out of range
        if index > self.length:
            print("ERROR: 'Get' Index out of range!")
            return None
        # Counter starts at 0 because we start our cursor at the head
        cur_idx = 0
        # Start at head
        cur = self.head
        # Iterate through singly LL
        while cur != None:
            if cur_idx == index:
                return cur
            cur = cur.next
            cur_idx += 1

    def erase(self, index):
        # Check that index isnt out of range
        if index > self.length:
            print("ERROR: 'Erase' Index out of range!")
            return None
        # Counter for current index
        cur_idx = 0

        # Start at head
        cur = self.head

        # Iterate through singly LL
        while cur_idx < self.length:
            # Base case: check if we're at index we're looking for
            if cur_idx == index:

                # If at the head
                if self.head == cur:

                    # If there is no following node, set head as an empty node
                    if cur.next == None:
                        self.head = node()

                    # Otherwise, set the head as the following node and decrement length
                    self.head = cur.next
                    self.length -= 1
                    return

                # If not at head, get the prev node using get()
                prev = self.get(cur_idx - 1)

                # If there is no following node, set prev.next = None
                if cur.next == None:
                    prev.next = None

                # Otherwise, set prev.next to the following node
                else:
                    prev.next = cur.next

                # Decrement length
                self.length -= 1
                return

            #If not at the index we're looking for, increment current node and index
            cur = cur.next
            cur_idx += 1

