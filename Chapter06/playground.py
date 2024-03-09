class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None

    def get_data(self):
        return self.data

    def get_left_node(self):
        return self.left_child

    def get_right_node(self):
        return self.right_child


n1 = Node("root node")
n2 = Node("left child node")
n3 = Node("right child node")
n4 = Node("left grandchild node")

n1.left_child = n2
n1.right_child = n3
n2.left_child = n4


def inorder_traversal(node: Node):
    if node.get_left_node() is not None:
        inorder_traversal(node.get_left_node())

    print(node.get_data(), end=' ')

    if node.get_right_node() is not None:
        inorder_traversal(node.get_right_node())


inorder_traversal(n1)
