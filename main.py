from Tree import Tree

def main():
    tree = Tree()
    tree.push(1)
    tree.push(2)
    tree.push(3)
    tree.push(4)
    tree.push(5)
    print("Tree\n", tree)
    print("inorder")
    print(tree.inorder())
    print("preorder")
    print(tree.preorder())
    print("postorder")
    print(tree.postorder())

    avl_tree = Tree(True)
    avl_tree.push(1)
    avl_tree.push(2)
    avl_tree.push(3)
    avl_tree.push(4)
    avl_tree.push(5)

    print("\nAVL Tree\n",avl_tree)
    print("inorder")
    print(avl_tree.inorder())
    print("preorder")
    print(avl_tree.preorder())
    print("postorder")
    print(avl_tree.postorder())

if __name__ == "__main__":
    main()