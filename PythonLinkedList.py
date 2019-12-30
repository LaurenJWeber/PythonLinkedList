###############################################################################
# Description: Singly-linked list with methods for appending, inserting,
# removing nodes etc.
# Author: Lauren J Weber
###############################################################################


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

    def append_node(self, value):
        """ Add a node to the end of the list.
            Return the head node.
        """

        # Empty list
        if self.head is None:
            self.head = Node(value)
        else:
            new_node = Node(value)
            temp_node = self.head

            while temp_node.nextNode is not None:
                temp_node = temp_node.nextNode

            temp_node.nextNode = new_node

        return self.head

    def get_last_node(self):
        """ Return the last node in the list. """

        if self.head is None:
            return None

        temp = self.head

        while temp.nextNode is not None:
            temp = temp.nextNode

        return temp

    def append_node_given_last(self, value, last_node):
        """ Add a node to the end of the list.
            Return the last node in the list.
        """

        new_node = Node(value)
        last_node.nextNode = new_node
        return new_node

    def print_list_contents(self):
        """ Print the contents of the list. """

        print("Contents:")

        if self.head is None:
            return

        temp = self.head
        print(temp.value)

        while temp.nextNode is not None:
            temp = temp.nextNode
            print(temp.value)

    def get_node_count(self):
        """ Return the number of nodes in the list """

        node_count = 0

        if self.head is None:
            return node_count
        else:
            temp = self.head
            node_count += 1

            while temp.nextNode is not None:
                temp = temp.nextNode
                node_count += 1

        return node_count

    def get_value_at_position(self, index):
        """ Return the value of a node at the specified position."""
        if self.get_node_count() == 0 or index < 0 or index >= self.get_node_count():
            return None

        temp = self.head
        counter = 0

        while temp.nextNode is not None and counter < index:
            temp = temp.nextNode
            counter += 1

        return temp.value

    def set_value_at_position(self, value, index):
        """ Set the value of a node at the specified position. """
        if self.get_node_count() == 0 or index < 0 or index >= self.get_node_count():
            return False

        temp = self.head
        counter = 0

        if index == 0:
            self.head.value = value
            return True

        while temp.nextNode is not None and counter < index:
            temp = temp.nextNode
            counter += 1
            temp.value = value
            print("Set value at", counter, "to", value)

        return True

    def insert_node_at_position(self, value, index):
        """ Insert a node into the list at the specified position. """
        if index < 0 or index > self.get_node_count():
            return None

        new_node = Node(value)

        # Special case: inserting at head of list.
        if index == 0:
            new_node.nextNode = self.head
            self.head = new_node
        else:
            temp = self.head
            counter = 0

            while temp.nextNode is not None and counter < index - 1:
                temp = temp.nextNode
                counter += 1

            new_node.nextNode = temp.nextNode
            temp.nextNode = new_node
        return new_node

    def get_head_node(self):
        """ Return the head node in the list. """
        return self.head

    def get_node_after(self, node):
        """ Return the node after the given node. """
        if node.nextNode is None:
            return None

        return node.nextNode

    def remove_head_node(self):
        """ Remove the first (head) node from the list.
            Return the new head node
        """

        # Empty list
        if self.head is None:
            return None

        # List with single element
        if self.head.nextNode is None:
            self.head = None
            return None

        self.head = self.head.nextNode

        return self.head

    def remove_node_after(self, node):
        """ Remove the node after the specified node. """

        # We are already at the last node in the list.
        if node.nextNode is None:
            return node

        next_node = node.nextNode

        # We're at the penultimate node in the list.
        if next_node.nextNode is None:
            node.nextNode = None
            return node

        node.nextNode = next_node.nextNode
        return node

    def remove_all_nodes_with_value(self, value_to_remove):
        """ Remove all nodes with the specified value """

        if self.head is None:
            return

        while self.head is not None and self.head.value == value_to_remove:
            self.remove_head_node()

        if self.head is None:
            return

        temp = self.head
        while temp is not None and temp.nextNode is not None:
            if temp.nextNode.value == value_to_remove:
                self.remove_node_after(temp)
            else:
                temp = temp.nextNode

    def remove_duplicate_values(self):
        """ Remove duplicate values from the list. Use a python
            built-in list as an additional temporary data structure. """

        values_in_linked_list = []

        if self.head is None:
            return

        values_in_linked_list.append(self.head.value)

        temp = self.head
        while temp is not None and temp.nextNode is not None:
            if temp.nextNode.value in values_in_linked_list:
                self.remove_node_after(temp)
            else:
                values_in_linked_list.append(temp.nextNode.value)
                temp = temp.nextNode

    def remove_duplicate_values_use_hashtable(self):
        """ Remove duplicate values from the list.
            Use a dictionary (hash table) as an additional data structure. """

        values_dictionary = {}

        if self.head is None:
            return

        values_dictionary[self.head.value] = True

        temp = self.head
        while temp is not None and temp.nextNode is not None:
            if temp.nextNode.value in values_dictionary.keys():
                self.remove_node_after(temp)
            else:
                values_dictionary[temp.nextNode.value] = True
                temp = temp.nextNode

    def append_nodes(self, py_list):
        """ Append a list of values to the linked list. """

        for val in py_list:
            self.append_node(val)

    def append_nodes_optimized(self, py_list):
        """ Append a list of values to the linked list.
            After appending each value, return the last node in the list rather than the head,
            to reduce the runtime of each operation from O(N) to O(1). """

        if len(py_list) <= 0:
            return

        last_node = self.get_last_node()

        if last_node is None:
            last_node = self.append_node(py_list[0])
            if len(py_list) > 1:
                for val in py_list[1:]:
                    last_node = self.append_node_given_last(val, last_node)
        else:
            if len(py_list) > 1:
                for val in py_list:
                    last_node = self.append_node_given_last(val, last_node)

    def compare_to(self, list2):
        """ Compare two linked lists.  Return true if:
            Lists are the same length, and
            Values at each position are the same in both lists.
        """

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
