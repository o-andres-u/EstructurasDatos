class Node:

    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.size = 0
        self.root = None

    def _insert_recursive(self, node, element):
        if node is None:
            new_node = Node(element)
            if self.size == 0:
                self.root = new_node
            self.size += 1
            return new_node
        if element < node.element:
            node.left = self._insert_recursive(node.left, element)
        else:
            node.right = self._insert_recursive(node.right, element)
        return node

    def insert(self, element):
        self._insert_recursive(self.root, element)

    def get_leaves(self, node):
        if node is None:
            return 0

        if node.left is None and node.right is None:
            return 1

        left_leaves = self.get_leaves(node.left)
        right_leaves = self.get_leaves(node.right)

        return left_leaves + right_leaves


if __name__ == '__main__':
    cases = int(input())
    for case in range(cases):
        numbers = input().split()
        numbers.pop()
        bst = BST()
        for number in numbers:
            bst.insert(int(number))
        print(bst.get_leaves(bst.root))
