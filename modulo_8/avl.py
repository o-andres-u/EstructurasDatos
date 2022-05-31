from node import Node


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

    def _delete_recursive(self, root, element):
        if not root:
            return root
        elif element < root.element:
            root.left = self._delete_recursive(root.left, element)
        elif element > root.element:
            root.right = self._delete_recursive(root.right, element)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self._get_min(root.right)
            root.element = temp
            root.right = self._delete_recursive(root.right, temp)
        # if root is None:
        #     return root

        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))
        balance_factor = self._get_balance(root)

        if balance_factor > 1:
            if self._get_balance(root.left) >= 0:
                return self._rotate_right(root)
            else:
                root.left = self._rotate_left(root.left)
                return self._rotate_right(root)
        if balance_factor < -1:
            if self._get_balance(root.right) <= 0:
                return self._rotate_left(root)
            else:
                root.right = self._rotate_right(root.right)
                return self._rotate_left(root)
        return root

    def _search_recursive(self, root, element):
        if root is None or root.element == element:
            return root
        if element < root.element:
            return self._search_recursive(root.left, element)
        else:
            return self._search_recursive(root.right, element)

    def _get_min(self, root):
        if root is None:
            return None
        elif root.left is None:
            return root.element
        return self._get_min(root.left)

    def _get_max(self, root):
        if root is None:
            return None
        elif root.right is None:
            return root.element
        return self._get_max(root.right)

    def insert(self, element):
        if not self.search(element):
            self.root = self._insert_recursive(self.root, element)

    def search(self, element):
        return self._search_recursive(self.root, element) is not None

    def delete(self, element):
        self.size -= self.search(element)
        self.root = self._delete_recursive(self.root, element)

    def get_tree_height(self, element):
        root = self._search_recursive(self.root, element)
        return root.height if root else 0
