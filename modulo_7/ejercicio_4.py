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

    def print_dri(self, node, depth=0):
        if node is not None:
            self.print_dri(node.right, depth+1)
            print('\t'*depth+str(node.element))
            self.print_dri(node.left, depth+1)


if __name__ == '__main__':
    cases = int(input())
    for case in range(cases):
        numbers = input().split()
        numbers.pop()
        bst = BST()
        for number in numbers:
            bst.insert(number)
        bst.print_dri(bst.root)
        print()

        # 8 12 14 15 13 10 11 9 4 6 7 5 2 3 1 -1
