#!/usr/bin/python3
"""
Node Class
"""


class Node:
    """
    initialize the node obj
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return (self.__data)

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if value is None:
            self.__next_node = value
        elif isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


"""
Singly Linked List Class
- Creates a linked list of sorted Node objects and prints
"""


class SinglyLinkedList:
    """
    Initialize singly linked list obj
    """
    def __init__(self):
        self.__head = None

    """
    Insert sorted Node object
    """
    def sorted_insert(self, value):
        if self.__head is None or value < self.__head.data:
            self.__head = Node(value, self.__head)
            return
        tmp = self.__head
        while tmp.next_node is not None and tmp.next_node.data < value:
            tmp = tmp.next_node
        tmp.next_node = Node(value, tmp.next_node)
    """
    Print
    """
    def __str__(self):
        if self.__head is None:
            return ("")
        tmp = self.__head
        _list = ""
        while tmp is not None:
            _list += str(tmp.data)
            tmp = tmp.next_node
            if tmp is not None:
                _list += "\n"
        return (_list)
