# Task: Add a method to the Node class in order to allow us to do a depth-first iteration over it and all of it's children

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, node):
        self.children.append(node)


node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)
node_4 = Node(4)
node_5 = Node(5)
node_6 = Node(6)
node_7 = Node(7)

node_1.add_child(node_2)
node_1.add_child(node_3)

node_3.add_child(node_4)

node_2.add_child(node_5)
node_2.add_child(node_6)

node_6.add_child(node_7)

# 1
# |  \
# 2    3
# | \    \
# 5  6     4
#    |
#    7

result = [n.value for n in node_1]

expected = [1, 2, 5, 6, 7, 3, 4]

assert result == expected
