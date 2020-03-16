# This node class will be handled by the Linked List that contains data, a next pointer, and a previous pointer
class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

# A double Linked List that has a head node reference, a tail node reference, and a length
class DoublyLinkedList:
    def __init__(self):
        self.head = node()
        self.tail = self.head
        self.length = 0

    # Appending creates a new node that is added to the end of the Linked List
    def append(self, data):
        new_node = node(data)
        # Add the new node to the end of the tail
        new_node.prev = self.tail
        self.tail.next = new_node
        # Set new node as new tail and add length
        self.tail = new_node
        self.length += 1
        return print("%s was added to Linked List. Length is now %d" %(str(data),self.length))

    # For each node in the Linked List, collect the data in order and print the list
    def display(self):
        cur = self.head
        elems = []
        while cur.next != None:
            cur = cur.next
            elems.append(cur.data)
        print(elems)

    # Display the Linked list in reverse order
    def display_reverse(self):
        cur = self.tail
        elems = []
        while cur.prev != None:
            elems.append(cur.data)
            cur = cur.prev
        print(elems)

    # Return the data for the node at given index in Linked List
    def get(self,index):
        # 0 =< index < length
        if index >= self.length or index < 0:
            print("ERROR: Index out of range!")
            return None
        # Start at head node and iterate through Linked List
        cur = self.head
        cur_idx = -1
        # As long as there is a next node, iterate and check if the next node is the ask
        while cur.next != None:
            cur_idx+=1
            cur = cur.next
            if cur_idx == index: return print(cur.data)

    # Remove a node from the Linked List at the given index
    def erase(self, index):
        if index >= self.length or index < 0:
            print("ERROR: Index out of range!")
            return None
        # If the index is the tail, prev is new tail, set no node after, and decrease length by 1
        if index == self.length - 1:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return print("%s was removed from index %d. Length is now %d" %(str(self.tail.data),index,self.length))
        # Iterate through Linked List starting at head
        cur = self.head
        cur_idx = -1
        # As long as there's a node after, find index then rewrite previous node to skip current node to next
        # And decrease length by 1
        while cur.next != None:
            last_node = cur
            cur_idx += 1
            cur = cur.next
            if cur_idx == index:
                last_node.next = cur.next
                cur.next.prev = last_node
                self.length -= 1
                return print("%s was removed from index %d. Length is now %d" %(str(cur.data),index, self.length))

