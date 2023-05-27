class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class Tree:
    def __init__(self):
        self.root = None

    def __str__(self):
        return f"In-order: {self.inorder()}\n"+\
               f"Pre-order: {self.preorder()}\n"+\
               f"Post-order: {self.postorder()}"
    
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

    # public algorithms to retrieve the order in a list
    def inorder(self):
        result = []
        self.__inorder(self.root, result)
        return result

    def preorder(self):
        result = []
        self.__preorder(self.root, result)
        return result

    def postorder(self):
        result = []
        self.__postorder(self.root, result)
        return result
    
    # private recursive algorithms to traverse the tree
    def __inorder(self, root, result):
        if root:
            self.__inorder(root.left, result)
            result.append(root.value)
            self.__inorder(root.right, result)
    
    def __preorder(self, root, result):
        if root:
            result.append(root.value)
            self.__preorder(root.left, result)
            self.__preorder(root.right, result)
    
    def __postorder(self, root, result):
        if root:
            self.__postorder(root.left, result)
            self.__postorder(root.right, result)
            result.append(root.value)