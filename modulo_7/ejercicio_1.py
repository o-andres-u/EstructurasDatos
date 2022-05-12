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

    def pre_order(self, node):
        print(node.element, end=' ')
        if node.left is not None:
            self.pre_order(node.left)
        if node.right is not None:
            self.pre_order(node.right)


if __name__ == '__main__':
    cases = int(input())
    for case in range(cases):
        values = list(map(int, input().split()))
        values.pop()
        bst = BST()
        for value in values:
            bst.insert(value)
        bst.pre_order(bst.root)
        print()
