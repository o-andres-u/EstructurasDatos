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

    # https://favtutor.com/blogs/binary-tree-height
    def calculate_height(self, node):
        if node is None:
            return 0
        left_height = self.calculate_height(node.left)
        right_height = self.calculate_height(node.right)

        return max(left_height, right_height) + 1


if __name__ == '__main__':
    cases = int(input())
    for case in range(cases):
        numbers = input().split()
        numbers.pop()
        bst = BST()
        for number in numbers:
            bst.insert(int(number))
        print(bst.calculate_height(bst.root))
