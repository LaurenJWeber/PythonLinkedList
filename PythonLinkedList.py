###############################################################################
# Implementation of a single node.
###############################################################################


class Node:

    def __init__(self, value):
        self.value = value
        self.nextNode = None


###############################################################################
# Implementation of singly-linked list data structure.
###############################################################################

class LinkedList:

    def __init__(self):
        self.head = None

    #########################################
    # Add a node to the end of the list.
    #########################################
    def append_node(self, value):

        # Empty list
        if self.head is None:
            self.head = Node(value)
        else:
            newNode = Node(value)
            tempNode = self.head

            while tempNode.nextNode is not None:
                tempNode = tempNode.nextNode

            tempNode.nextNode = newNode
            return self.head

    #########################################
    # Print the contents of the list.
    #########################################
    def print_list_contents(self):
        print("Contents:")

        if self.head is None:
            return

        temp = self.head
        print(temp.value)

        while temp.nextNode is not None:
            temp = temp.nextNode
            print(temp.value)

    #########################################
    # Get the number of nodes in the list.
    #########################################
    def get_node_count(self):

        nodeCount = 0

        if self.head is None:
            return nodeCount
        else:
            temp = self.head
            nodeCount += 1

            while temp.nextNode is not None:
                temp = temp.nextNode
                nodeCount += 1

        return nodeCount

    ####################################################
    # Get the value of a node at the specified position.
    ####################################################
    def get_value_at_position(self, index):
        if self.get_node_count() == 0 or index < 0 or index >= self.get_node_count():
            return None

        temp = self.head
        counter = 0

        while temp.nextNode is not None and counter < index:
            temp = temp.nextNode
            counter += 1

        return temp.value

    ####################################################
    # Set the value of a node at the specified position.
    ####################################################
    def set_value_at_position(self, value, index):
        if self.get_node_count() == 0 or index < 0 or index >= self.get_node_count():
            return False

        temp = self.head
        counter = 0

        while temp.nextNode is not None and counter < index:
            temp = temp.nextNode
            counter += 1
            temp.value = value

        return True

    ########################################################
    # Insert a node into the list at the specified position.
    ########################################################
    def insert_node_at_position(self, value, index):
        if index < 0 or index > self.get_node_count():
            return False

        newNode = Node(value)

        # Special case: inserting at head of list.
        if index == 0:
            newNode.nextNode = self.head
            self.head = newNode
        else:
            temp = self.head
            counter = 0

            while temp.nextNode is not None and counter < index - 1:
                temp = temp.nextNode
                counter += 1

            newNode.nextNode = temp.nextNode
            temp.nextNode = newNode

        # Todo: return the node if inserted successfully.
        return True

    ########################################################
    # Return the head node in the list.
    ########################################################
    def get_head_node(self):
        return self.head

    ########################################################
    # Return the node after the given node.
    ########################################################
    def get_node_after(self, node):
        if node.nextNode is None:
            return None

        return node.nextNode

    ########################################################
    # Remove the first (head) node from the list.
    ########################################################
    def remove_head_node(self):

        # Empty list
        if self.head is None:
            return None

        # List with single element
        if self.head.nextNode is None:
            self.head = None
            return None

        self.head = self.head.nextNode

        return self.head

    ########################################################
    # Remove the node after the specified node.
    ########################################################
    def remove_node_after(self, node):

        # We are already at the last node in the list.
        if node.nextNode is None:
            return node

        next = node.nextNode

        # We're at the penultimate node in the list.
        if next.nextNode is None:
            node.nextNode = None
            return node

        node.nextNode = next.nextNode
        return node

    ########################################################
    # Remove all nodes with the specified value
    ########################################################
    def remove_all_nodes_with_value(self, valueToRemove):

        if self.head is None:
            return

        while self.head is not None and self.head.value == valueToRemove:
            self.remove_head_node()

        if self.head is None:
            return

        temp = self.head
        while temp is not None and temp.nextNode is not None:
            if temp.nextNode.value == valueToRemove:
                self.remove_node_after(temp)
            else:
                temp = temp.nextNode

    ########################################################
    # Remove duplicate values from the list
    ########################################################
    def remove_duplicate_values(self):

        valuesInLinkedList = []

        if self.head is None:
            return

        valuesInLinkedList.append(self.head.value)

        temp = self.head
        while temp is not None and temp.nextNode is not None:
            if temp.nextNode.value in valuesInLinkedList:
                self.remove_node_after(temp)
            else:
                valuesInLinkedList.append(temp.nextNode.value)
                temp = temp.nextNode

    ########################################################
    # Append a list of values to the linked list.
    ########################################################
    def append_nodes(self, pyList):

        for val in pyList:
            self.append_node(val)

    ######################################################
    # Compare two linked lists.  Return true if:
    # Lists are the same length and
    # Values at each position are the same in both lists.
    #######################################################

    def compare_to(self, list2):

        length = self.get_node_count()

        if length != list2.get_node_count():
            return False

        # Both lists length 0 (no nodes, null head).  No further comparison needed.
        if length == 0:
            return True

        for i in range(0, length):
            if self.get_value_at_position(i) != list2.get_value_at_position(i):
                return False

        return True
