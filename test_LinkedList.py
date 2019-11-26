################################
# Tests for LinkedList class
################################

import pytest
from PythonLinkedList import LinkedList


@pytest.fixture
def linked_list():
    my_linked_list = LinkedList()
    return my_linked_list

###########################################
# Get the contents of a LinkedList object
# and store them in an array (python list)
###########################################


def linked_list_values_to_array(linkedList):
    contents = []
    for i in range(0, linkedList.get_node_count()):
        contents.append(linkedList.get_value_at_position(i))
    return contents

##########################################
# Unit tests!
##########################################


def test_empty_list():
    my_linked_list = LinkedList()
    assert my_linked_list.get_node_count() == 0
    assert my_linked_list.get_head_node() is None
    assert my_linked_list.get_value_at_position(0) is None
    assert my_linked_list.get_value_at_position(1) is None


def test_single_node():
    my_linked_list = LinkedList()
    my_linked_list.append_node(0)
    assert my_linked_list.get_node_count() == 1
    assert my_linked_list.get_head_node().value == 0
    assert my_linked_list.get_value_at_position(0) == 0
    assert my_linked_list.get_value_at_position(1) is None
    assert my_linked_list.get_value_at_position(1) is None


def test_remove_head_node_empty_list():
    my_linked_list = LinkedList()
    my_linked_list.remove_head_node()
    assert my_linked_list.get_node_count() == 0
    assert my_linked_list.get_head_node() is None  


def test_remove_head_node_length1():
    my_linked_list = LinkedList()
    my_linked_list.append_node(0)
    my_linked_list.remove_head_node()
    assert my_linked_list.get_node_count() == 0
    assert my_linked_list.get_head_node() is None
    assert my_linked_list.get_value_at_position(0) is None    


def test_remove_head_node_length2():
    my_linked_list = LinkedList()
    my_linked_list.append_nodes([0, 1])
    my_linked_list.remove_head_node()
    assert my_linked_list.get_node_count() == 1
    assert my_linked_list.get_head_node().value == 1    
    assert my_linked_list.get_value_at_position(0) == 1
    assert my_linked_list.get_value_at_position(1) is None


def test_remove_head_node_length3():
    my_linked_list = LinkedList()
    my_linked_list.append_nodes([0, 1, 2])
    my_linked_list.remove_head_node()
    assert my_linked_list.get_node_count() == 2
    assert my_linked_list.get_head_node().value == 1 
    assert my_linked_list.get_value_at_position(1) == 2   


def test_get_value_at_position():
    my_linked_list = LinkedList()
    inputValues = [0, 1, 2, 3, 4, 5]
    my_linked_list.append_nodes(inputValues)
    outputValues = linked_list_values_to_array(my_linked_list)
    assert inputValues == outputValues


def test_remove_all_nodes_with_value_empty():
    my_linked_list = LinkedList()
    my_linked_list.remove_all_nodes_with_value(0)
    assert my_linked_list.get_node_count() == 0
    assert my_linked_list.get_head_node() is None
    assert my_linked_list.get_value_at_position(0) is None
    assert my_linked_list.get_value_at_position(1) is None


def test_remove_all_nodes_with_value_length1():
    my_linked_list = LinkedList()
    my_linked_list.append_node(0)
    my_linked_list.remove_all_nodes_with_value(1)
    assert my_linked_list.get_node_count() == 1
    assert my_linked_list.get_head_node().value == 0
    assert my_linked_list.get_value_at_position(0) == 0
    my_linked_list.remove_all_nodes_with_value(0)
    assert my_linked_list.get_node_count() == 0
    assert my_linked_list.get_head_node() is None
    assert my_linked_list.get_value_at_position(0) is None


def test_remove_all_nodes_with_value_length2():
    my_linked_list = LinkedList()
    my_linked_list.append_nodes([0, 1])
    my_linked_list.remove_all_nodes_with_value(1)
    assert my_linked_list.get_node_count() == 1
    assert my_linked_list.get_head_node().value == 0
    my_linked_list.append_node(1)
    my_linked_list.remove_all_nodes_with_value(0)
    assert my_linked_list.get_node_count() == 1
    assert my_linked_list.get_head_node().value == 1
    assert my_linked_list.get_value_at_position(2) is None


def test_remove_all_nodes_with_value_multiple():
    my_linked_list = LinkedList()
    inputValues = [0, 1, 2, 3, 0, 4, 5, 6, 0, 7, 8, 9, 0]
    expectedOutputValues = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    my_linked_list.append_nodes(inputValues)
    my_linked_list.remove_all_nodes_with_value(0)
    actualOutputValues = linked_list_values_to_array(my_linked_list)
    assert expectedOutputValues == actualOutputValues


def test_remove_all_nodes_with_value_multiple_at_start_and_end():
    my_linked_list = LinkedList()
    inputValues = [0, 0, 0, 0, 0, 1, 0, 2, 3, 0, 4, 5, 6, 0, 7, 8, 9, 0, 0, 0]
    expectedOutputValues = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    my_linked_list.append_nodes(inputValues)
    my_linked_list.remove_all_nodes_with_value(0)
    actualOutputValues = linked_list_values_to_array(my_linked_list)
    assert expectedOutputValues == actualOutputValues


def test_remove_all_nodes_with_value_not_in_list():
    my_linked_list = LinkedList()
    inputValues = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    my_linked_list.append_nodes(inputValues)
    my_linked_list.remove_all_nodes_with_value(0)
    expectedOutputValues = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    actualOutputValues = linked_list_values_to_array(my_linked_list)
    assert expectedOutputValues == actualOutputValues


def test_remove_duplicate_values_empty():
    my_linked_list = LinkedList()
    my_linked_list.remove_duplicate_values()
    assert my_linked_list.get_node_count() == 0
    assert my_linked_list.get_head_node() is None
    assert my_linked_list.get_value_at_position(0) is None


def test_remove_duplicate_values_length1():
    my_linked_list = LinkedList()
    my_linked_list.append_node(0)
    my_linked_list.remove_duplicate_values()
    assert my_linked_list.get_node_count() == 1
    assert my_linked_list.get_head_node().value == 0
    assert my_linked_list.get_value_at_position(0) == 0
    

def test_remove_duplicate_values_length2():
    my_linked_list = LinkedList()
    my_linked_list.append_nodes([0, 0])
    my_linked_list.remove_duplicate_values()
    assert my_linked_list.get_node_count() == 1
    assert my_linked_list.get_head_node().value == 0
    assert my_linked_list.get_value_at_position(0) == 0
    my_linked_list.append_node(1)
    my_linked_list.remove_duplicate_values()
    assert my_linked_list.get_node_count() == 2
    assert my_linked_list.get_value_at_position(0) == 0
    assert my_linked_list.get_value_at_position(1) == 1


def test_remove_duplicate_values_multiple():
    my_linked_list = LinkedList()
    inputValues = [0, 0, 1, 1, 2, 2, 3, 0, 1, 2, 3, 4, 5, 6, 5, 7, 8, 9, 1, 0, 0, 0]
    my_linked_list.append_nodes(inputValues)
    my_linked_list.remove_duplicate_values()
    expectedOutputValues = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    actualOutputValues = linked_list_values_to_array(my_linked_list)
    assert expectedOutputValues == actualOutputValues


def test_get_value_at_position_multiple(linked_list):
    my_linked_list = linked_list
    inputValues = []
    lower = 0
    upper = 100
    for i in range(lower, upper):
        inputValues.append(i)
    
    my_linked_list.append_nodes(inputValues)
    outputValues = linked_list_values_to_array(my_linked_list)
    assert inputValues == outputValues


def test_compare_lists_empty():
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()
    assert linked_list_1.compare_to(linked_list_2)
  
    
def compare_lists_length1():
    linked_list_1 = LinkedList()
    linked_list_1.append_node(0)
    linked_list_2 = LinkedList()
    linked_list_2.append_node(0)
    assert linked_list_1.compare_to(linked_list_2)
    linked_list_2.set_value_at_position(1, 0)
    assert not linked_list_1.compare_to(linked_list_2)

# Todo: 
# DONE - create
# DONE - append
# DONE - get number of elements
# DONE - print contents
# DONE - remove head
# DONE - remove node after
# DONE - remove all nodes_with_value(value)
# DONE - remove_duplicate_values()
# DONE - append a node for each value in a my_linked_list - make testing faster and more compact.
# DONE - get value at position
# DONE - Compare two lists - same length, same values in each node.
# DONE - Install pytest, write first unit tests for LinkedList class.
# DONE - Convert rest of tests to pytest.
# DONE - Convert to python 3

# Unit tests for set_value_at_position()
# look into markers - empty, length1, length > 1
# look more into fixtures.
# insert at position
# remove_node_at_position()
# remove_first_node_with_value(value)
# Make remove nodes call a common sub-function?

