class node:
    def __init__(self,value=None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None

class binary_search_tree:
    def __init__(self):
        self.root = None

    # insert elements to bst
    def insert(self,value):
        if self.root == None:
            self.root = node(value)
        else:
            self._insert(value,self.root)

    def _insert(self,value,cur_node):
        if value < cur_node.value:
            # check if current node has a left child already
            if cur_node.left_child == None:
                # if not, set left_child = new node with value
                cur_node.left_child = node(value)
                cur_node.left_child.parent = cur_node
            else:
                # if so, recurse down left part of tree
                self._insert(value,cur_node.left_child)
        elif value > cur_node.value:
            if cur_node.right_child == None:
                cur_node.right_child = node(value)
                cur_node.right_child.parent = cur_node
            else:
                self._insert(value,cur_node.right_child)
        else:
            print("Value already in tree!")

    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)

    def _print_tree(self,cur_node):
        if cur_node != None:
            # recursively start at the bottom-most left value (lowest) value
            self._print_tree(cur_node.left_child)
            # once at the bottom-most left, print it
            print(str(cur_node.value))
            # if there is a right sibbling, access it and print it as well
            self._print_tree(cur_node.right_child)

    def height(self):
        if self.root != None:
            return self._height(self.root,0)
        else:
            return 0

    def _height(self,cur_node,cur_height):
        if cur_node == None:
            return cur_height
        left_height = self._height(cur_node.left_child,cur_height+1)
        right_height = self._height(cur_node.right_child,cur_height+1)
        return max(left_height,right_height)

    def search(self,value):
        if self.root != None:
            return self._search(value,self.root)
        else:
            return None

    def _search(self, value, cur_node):
        if value == cur_node.value:
            return cur_node
        elif value < cur_node.value and cur_node.left_child != None:
            return self._search(value,cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child != None:
            return self._search(value,cur_node.right_child)
        return None

    def delete_value(self,value):
        return self.delete_node(self.search(value))

    def delete_node(self,node):
        # checks if node exists or value is found in tree
        if node == None or self.search(node.value)==None:
            print("Node to be deleted not found!")
            return None

        # returns the lowest value node
        def min_value_node(node):
            current = node
            while current.left_child != None:
                current = current.left_child
            return current

        # returns the number of children a node has
        def num_children(node):
            num = 0
            if node.left_child != None:
                num += 1
            if node.right_child != None:
                num += 1
            return num

        # store parent of node to be deleted
        node_parent = node.parent

        #store number of children that node to be deleted has
        node_children = num_children(node)

        # Case 1: node has no children
        if node_children == 0:
            if node_parent != None:
                # remove reference from parent to node to be deleted
                if node_parent.left_child == node:
                    node_parent.left_child = None
                else:
                    node_parent.right_child = None
            else:
                self.root = None
        # Case 2: node has a single child
        if node_children == 1:
            #Store either the left or right child
            if node.left_child != None:
                child = node.left_child
            else:
                child = node.right_child

            # refer parent node to child
            if node_parent != None:
                if node_parent.left_child == node:
                    node_parent.left_child = child
                    child.parent = node_parent
                else:
                    node_parent.right_child = child
                    child.parent = node_parent
            else:
                self.root = child

        # Case 3: node has two children
        if node_children == 2:
            # get inorder successor of deleted node
            successor = min_value_node(node.right_child)

            #copy lowest value on right brand into node to be deleted
            node.value = successor.value

            #remove the successor node
            self.delete_node(successor)
