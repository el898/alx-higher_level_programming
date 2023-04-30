#!/usr/bin/python3
"""define class of a singly linked list"""


class Node:
    """Represent a node in a singly-linked list."""

    def __init__(self, data=None):
        """Initialize the  Node object.
        Args:
            data (int): The data of the new Node. Default is None.
            next_node (Node): refer to the next Node,Default is None.
        """
        self.__data = data
        self.__next_node = None

    @property
    def data(self):
        """Get/set the data of the Node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the Node.
        Args:
            value (int): The new data value to set for the Node.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """retrieve the reference to the next Node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next_node of the Node.
        Args:
            value (Node): The new Node object to set as the next node.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represent a singly-linked list."""

    def __init__(self):
        """Initialize an empty SinglyLinkedList object."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.
        The node is inserted into the list at the correct
        ordered numerical position.
        Args:
            value (int): The data value of the new Node.
        """
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and \
                    current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Method to generate a string representation.
        Returns:
            str: A string representation of the list.
        """
        nodes = []
        current = self.__head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)
