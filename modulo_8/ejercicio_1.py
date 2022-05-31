class Node(object):

    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None
        self.height = 1


class AVL(object):

    def __init__(self):
        self.size = 0
        self.root = None

    def _insert_recursive(self, root, element):
        if not root:
            new_node = Node(element)
            self.size += 1
            return new_node
        elif element < root.element:
            root.left = self._insert_recursive(root.left, element)
        else:
            root.right = self._insert_recursive(root.right, element)

        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))
        balance_factor = self._get_balance(root)
        if balance_factor > 1:
            if element < root.left.element:
                return self._rotate_right(root)
            else:
                root.left = self._rotate_left(root.left)
                return self._rotate_right(root)

        if balance_factor < -1:
            if element > root.right.element:
                return self._rotate_left(root)
            else:
                root.right = self._rotate_right(root.right)
                return self._rotate_left(root)

        return root

    def _get_height(self, root):
        if not root:
            return 0
        return root.height

    def _get_balance(self, root):
        if not root:
            return 0
        return self._get_height(root.left) - self._get_height(root.right)

    def _rotate_right(self, node):
        left = node.left
        aux = left.right
        left.right = node
        node.left = aux
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        left.height = 1 + max(self._get_height(left.left), self._get_height(left.right))
        return left

    def _rotate_left(self, node):
        right = node.right
        aux = right.left
        right.left = node
        node.right = aux
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        right.height = 1 + max(self._get_height(right.left), self._get_height(right.right))
        return right

    def insert(self, element):
        self.root = self._insert_recursive(self.root, element)

    def print_post_order(self, node):
        if node.left is not None:
            self.print_post_order(node.left)
        if node.right is not None:
            self.print_post_order(node.right)
        print(node.element, end='')


if __name__ == '__main__':
    for i in range(int(input())):
        entries = input().split()
        entries.pop()
        avl = AVL()
        for entry in entries:
            avl.insert(entry)
        avl.print_post_order(avl.root)
        print()
