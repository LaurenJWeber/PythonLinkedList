###############################################################################
# Description: Tests for LinkedList implementation.
# Prerequisites: Install pytest using PIP.
# Author: Lauren J Weber
###############################################################################

import pytest
from PythonLinkedList import LinkedList
from datetime import datetime


@pytest.fixture
def linked_list():
    my_linked_list = LinkedList()
    return my_linked_list

#####################################################
# Get the contents of a LinkedList object
# and store them in an array (python built-in list).
#####################################################


def linked_list_values_to_array(linked_list):
    contents = []
    for i in range(0, linked_list.get_node_count()):
        contents.append(linked_list.get_value_at_position(i))
    return contents

#####################################################
# Unit tests!
#####################################################


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
    input_values = [0, 1, 2, 3, 4, 5]
    my_linked_list.append_nodes(input_values)
    output_values = linked_list_values_to_array(my_linked_list)
    assert input_values == output_values


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
    input_values = [0, 1, 2, 3, 0, 4, 5, 6, 0, 7, 8, 9, 0]
    expected_output_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    my_linked_list.append_nodes(input_values)
    my_linked_list.remove_all_nodes_with_value(0)
    actual_output_values = linked_list_values_to_array(my_linked_list)
    assert expected_output_values == actual_output_values


def test_remove_all_nodes_with_value_multiple_at_start_and_end():
    my_linked_list = LinkedList()
    input_values = [0, 0, 0, 0, 0, 1, 0, 2, 3, 0, 4, 5, 6, 0, 7, 8, 9, 0, 0, 0]
    expected_output_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    my_linked_list.append_nodes(input_values)
    my_linked_list.remove_all_nodes_with_value(0)
    actual_output_values = linked_list_values_to_array(my_linked_list)
    assert expected_output_values == actual_output_values


def test_remove_all_nodes_with_value_not_in_list():
    my_linked_list = LinkedList()
    input_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    my_linked_list.append_nodes(input_values)
    my_linked_list.remove_all_nodes_with_value(0)
    expected_output_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    actual_output_values = linked_list_values_to_array(my_linked_list)
    assert expected_output_values == actual_output_values


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
    input_values = [0, 0, 1, 1, 2, 2, 3, 0, 1, 2, 3, 4, 5, 6, 5, 7, 8, 9, 1, 0, 0, 0]
    my_linked_list.append_nodes(input_values)
    my_linked_list.remove_duplicate_values()
    expected_output_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    actual_output_values = linked_list_values_to_array(my_linked_list)
    assert expected_output_values == actual_output_values


def test_remove_duplicate_values_with_hash_table_multiple():
    my_linked_list = LinkedList()
    input_values = [0, 0, 1, 1, 2, 2, 3, 0, 1, 2, 3, 4, 5, 6, 5, 7, 8, 9, 1, 0, 0, 0]
    my_linked_list.append_nodes(input_values)
    my_linked_list.remove_duplicate_values_use_hashtable()
    expected_output_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    actual_output_values = linked_list_values_to_array(my_linked_list)
    assert expected_output_values == actual_output_values


def test_get_value_at_position_multiple(linked_list):
    my_linked_list = linked_list
    input_values = []
    lower = 0
    upper = 100
    for i in range(lower, upper):
        input_values.append(i)
    
    my_linked_list.append_nodes(input_values)
    output_values = linked_list_values_to_array(my_linked_list)
    assert input_values == output_values


def test_compare_lists_empty():
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()
    assert linked_list_1.compare_to(linked_list_2)
  
    
def test_compare_lists_length1():
    linked_list_1 = LinkedList()
    linked_list_1.append_node(0)
    linked_list_2 = LinkedList()
    linked_list_2.append_node(0)
    assert linked_list_1.compare_to(linked_list_2)
    linked_list_2.set_value_at_position(1, 0)
    assert not linked_list_1.compare_to(linked_list_2)


def test_compare_lists_length2():
    linked_list_1 = LinkedList()
    linked_list_1.append_node(0)
    linked_list_1.append_node(1)
    linked_list_2 = LinkedList()
    linked_list_2.append_node(0)
    linked_list_2.append_node(1)
    assert linked_list_1.compare_to(linked_list_2)
    linked_list_2.set_value_at_position(2, 1)
    assert not linked_list_1.compare_to(linked_list_2)


def test_compare_lists_multiple():
    linked_list_1 = LinkedList()
    linked_list_1.append_nodes([0, 1, 2, 3, 4, 5, 6])
    linked_list_2 = LinkedList()
    linked_list_2.append_nodes([0, 1, 2, 3, 4, 5, 6])
    assert linked_list_1.compare_to(linked_list_2)
    linked_list_2.set_value_at_position(10, 0)
    assert not linked_list_1.compare_to(linked_list_2)
    linked_list_2.remove_head_node()
    assert not linked_list_1.compare_to(linked_list_2)


def test_append_optimized():
    py_list_empty = []
    py_list_len_1 = [0]
    py_list_len_2 = [0, 1]
    py_list_len_3 = [0, 1, 2]
    py_list_len_4 = [0, 1, 2, 3]

    linked_list_empty = LinkedList()
    linked_list_empty.append_nodes_optimized(py_list_empty)
    assert linked_list_empty.get_node_count() == 0

    linked_list_len_1 = LinkedList()
    linked_list_len_1.append_nodes_optimized(py_list_len_1)
    assert linked_list_values_to_array(linked_list_len_1) == py_list_len_1

    linked_list_len_2 = LinkedList()
    linked_list_len_2.append_nodes_optimized(py_list_len_2)
    assert linked_list_values_to_array(linked_list_len_2) == py_list_len_2

    linked_list_len_3 = LinkedList()
    linked_list_len_3.append_nodes_optimized(py_list_len_3)
    assert linked_list_values_to_array(linked_list_len_3) == py_list_len_3

    linked_list_len_4 = LinkedList()
    linked_list_len_4.append_nodes_optimized(py_list_len_4)
    assert linked_list_values_to_array(linked_list_len_4) == py_list_len_4


def initialize_array_with_duplicates(upper_bound_value, duplicate_sets):

    big_array = []

    for i in range(0, duplicate_sets):
        for j in range(0, upper_bound_value):
            big_array.append(j)

    return big_array

##############################################################################
# Profile the time to add a large set of values to a LinkedList when
# returning the head of the list after each addition,versus returning the
# last node after each addition.
#
# Also profile the time to remove duplicates from a linked list
# When using a build-in list as an additional data structure, vs. a
# dictionary (hash table) as an additional data structure.
#############################################################################


def main():
    sets_of_duplicates = 4
    max_value = 10000
    big_array = initialize_array_with_duplicates(max_value, sets_of_duplicates)

    linked_list_0_non_opt = LinkedList()
    ta = datetime.now()
    linked_list_0_non_opt.append_nodes(big_array)
    tb = datetime.now()
    append_time = tb - ta
    print("Time to prepare list non-optimized:", append_time)
    print("List size:", linked_list_0_non_opt.get_node_count())

    linked_list_1 = LinkedList()
    t0 = datetime.now()
    linked_list_1.append_nodes_optimized(big_array)
    t1 = datetime.now()
    append_time = t1 - t0
    print("Time to prepare list optimized:", append_time)
    print("List size:", linked_list_1.get_node_count())

    t2 = datetime.now()
    linked_list_1.remove_duplicate_values()
    t3 = datetime.now()
    dedup_time_list = t3 - t2
    print("Time to de-dup using built-in list as additional data structure:", dedup_time_list)
    print("Size of de-duped list:", linked_list_1.get_node_count())

    linked_list_2 = LinkedList()
    t4 = datetime.now()
    linked_list_2.append_nodes_optimized(big_array)
    t5 = datetime.now()
    append_time = t5 - t4
    print("Time to prepare list optimized:", append_time)
    print("List size:", linked_list_2.get_node_count())

    t6 = datetime.now()
    linked_list_2.remove_duplicate_values_use_hashtable()
    t7 = datetime.now()
    dedup_time_dict = t7 - t6
    print("Time to de-dup using dictionary as additional data structure:", dedup_time_dict)
    print("Size of de-duped list:", linked_list_2.get_node_count())


if __name__ == "__main__":
    main()
