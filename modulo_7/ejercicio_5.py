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

    # https://www.programiz.com/dsa/full-binary-tree
    def is_uva(self, root):
        if root is None:
            return True

        if root.left is None and root.right is None:
            return True

        if root.left is not None and root.right is not None:
            return self.is_uva(root.left) and self.is_uva(root.right)

        return False


if __name__ == '__main__':
    cases = int(input())
    for case in range(cases):
        numbers = input().split()
        numbers.pop()
        bst = BST()
        for number in numbers:
            bst.insert(int(number))
        if bst.is_uva(bst.root):
            print("racimo de uva")
        else:
            print("no es")
