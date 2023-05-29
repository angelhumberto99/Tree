class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def __str__(self):
        return f"[{self.left} <- {self.value} -> {self.right}]"

class Tree:
    def __init__(self, avl=False):
        self.root = None
        self.avl = avl

    def __str__(self):
        return self.root.__str__()
    
    def push(self, value):
        """Adds a new node to the tree"""
        if self.root is None:
            self.root = Node(value)
            return
        
        node = self.root
        while True:
            if value == node.value:
                node.value = value
                return
            if value > node.value:
                if node.right is None:
                    node.right = Node(value)
                    break
                node = node.right
            else:
                if node.left is None:
                    node.left = Node(value)
                    break
                node = node.left
        if self.avl:
            self.balance(self.root)

    def is_leaf(self, node):
        """Check if the given node is a leaf"""
        return (node is not None) and (node.left == node.right)

    def get_height(self, node):
        """Return the height of the given node"""
        if node is None or self.is_leaf(node):
            return 1
        else: 
            return max(self.get_height(node.left), self.get_height(node.right)) + 1
    
    def get_balance_factor(self, node):
        """Calculates the balance factor of the given node in order to make rotations"""
        return self.get_height(node.right) - self.get_height(node.left)

    def balance(self, node):
        """Performs rotations on the nodes when they unbalance the tree"""
        factor = self.get_balance_factor(node)
        if factor == -2:
            if self.get_balance_factor(node.left) == -1:
                self.root = self.simple_right_rotation(node)
            else:
                self.root = self.double_right_rotation(node)
        if factor == 2:
            if self.get_balance_factor(node.right) == 1:
                self.root = self.simple_left_rotation(node)
            else:
                self.root = self.double_left_rotation(node)

    def simple_left_rotation(self, node):
        """Rotate node to the left once"""
        aux1 = node.right
        aux2 = aux1.left

        node.right = aux2
        aux1.left = node
        return aux1

    def simple_right_rotation(self, node):
        """Rotate node to the right once"""
        aux1 = node.left
        aux2 = aux1.right

        node.left = aux2
        aux1.right = node
        return aux1
    
    def double_left_rotation(self, node):
        """Rotate node twice, once to the right and once to the left"""
        self.root.right = self.simple_right_rotation(node.right)
        return self.simple_left_rotation(self.root)

    def double_right_rotation(self, node):
        """Rotate node twice, once to the left and once to the right"""
        self.root.left = self.simple_left_rotation(node.left)
        return self.simple_right_rotation(self.root)

    # public algorithms to retrieve the order in a list
    def inorder(self):
        """Returns a list with the values of the tree in order"""
        result = []
        self.__inorder(self.root, result)
        return result

    def preorder(self):
        """Returns a list with the values of the tree in preorder"""
        result = []
        self.__preorder(self.root, result)
        return result

    def postorder(self):
        """Returns a list with the values of the tree in postorder"""
        result = []
        self.__postorder(self.root, result)
        return result
    
    # private recursive algorithms to traverse the tree
    def __inorder(self, root, result):
        """Traverse the tree nodes in order"""
        if root:
            self.__inorder(root.left, result)
            result.append(root.value)
            self.__inorder(root.right, result)
    
    def __preorder(self, root, result):
        """Traverse the tree nodes in preorder"""
        if root:
            result.append(root.value)
            self.__preorder(root.left, result)
            self.__preorder(root.right, result)
    
    def __postorder(self, root, result):
        """Traverse the tree nodes in postorder"""
        if root:
            self.__postorder(root.left, result)
            self.__postorder(root.right, result)
            result.append(root.value)