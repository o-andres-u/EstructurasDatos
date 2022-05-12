from node import Node


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

    @staticmethod
    def _find_min(node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def _delete_recursive(self, root, element):
        if root is None:
            return root
        if element < root.element:
            root.left = self._delete_recursive(root.left, element)
        elif element > root.element:
            root.right = self._delete_recursive(root.right, element)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = BST._find_min(root.right)
            root.element = temp.element
            root.right = self._delete_recursive(root.right, temp.element)
        return root

    def _search_recursive(self, root, element):
        if root is None or root.element == element:
            return root
        if element < root.element:
            return self._search_recursive(root.left, element)
        else:
            return self._search_recursive(root.right, element)

    def insert(self, element):
        self._insert_recursive(self.root, element)

    def search(self, element):
        return self._search_recursive(self.root, element) is not None

    def delete(self, element):
        self.size -= self.search(element)
        self.root = self._delete_recursive(self.root, element)
