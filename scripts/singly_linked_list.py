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
        if self.length == 0:
            return None

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
        if index >= self.length or index < 0:
            print("ERROR: 'Get' Index out of range!")
            return None

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
        if index >= self.length or index < 0:
            print("ERROR: Index out of range!")
            return None

        curr = self.get(index)

        # If at head node
        if self.head == curr:
            if curr.next == None:
                self.head = node()
            else:
                self.head = curr.next
        else:
            # Any non-head node
            prev = self.get(index - 1)
            if curr.next == None:
                prev.next = None
            else:
                prev.next = curr.next
        self.length -= 1
        return
