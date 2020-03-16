# This node class will be handled by the Linked List that contains data and a next pointer.
class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class singly_linked_list:
    def __init__(self):
        # Head node is created that stores no data but signals start of the singly LL
        self.head = node()
        self.tail = self.head

    def append(self, data):
        # Create new node
        new_node = node(data)
        # Point new node as following current tail
        self.tail.next = new_node
        # Set new node as the new tail
        self.tail = new_node

    def length(self):
        # Set pointer to head
        cur = self.head
        # Counter for nodes seen
        total = 0
        # Iterate through singly LL until you find the last node
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    def display(self):
        # Store data of each node in order
        elems = []
        # Start at head
        cur = self.head
        # Iterate through LL
        while cur.next != None:
            cur = cur.next
            elems.append(cur.data)
        print(elems)

    def get(self, index):
        # Check that index isnt out of range
        if index > self.length():
            print("ERROR: 'Get' Index out of range!")
            return None
        # Counter starts at -1 because we start our cursor at the head
        cur_idx = -1
        # Start at head
        cur = self.head
        # Iterate through singly LL
        while cur.next != None:
            cur = cur.next
            cur_idx += 1
            if cur_idx == index: return print(cur.data)

    def erase(self, index):
        # Check that index isnt out of range
        if index > self.length():
            print("ERROR: 'Erase' Index out of range!")
            return None
        # Counter for current index
        cur_idx = 0
        # Start at head
        cur = self.head
        # Iterate through singly LL
        while cur.next != None:
            # Store the cur node before incrementing
            last_node = cur
            # Increment current node
            cur = cur.next
            # When at index, point previous node to skip cur to next node
            if cur_idx == index:
                last_node.next = cur.next
                # If at the last node, set it as the tail
                if last_node.next == None:
                    self.tail = last_node
                return
            # Increment counter
            cur_idx += 1
