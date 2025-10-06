class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return

        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if current.left is None:
                current.left = new_node
                break
            else:
                queue.append(current.left)

            if current.right is None:
                current.right = new_node
                break
            else:
                queue.append(current.right)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")

if __name__ == "__main__":
    bt = BinaryTree()
    n = int(input("Enter the number of nodes to be in the binary tree: "))
    for i in range(n):
        val = int(input(f"Enter the value of node {i+1}: "))
        bt.insert(val)
    print("\nInorder Binary Tree:", end=" ")
    bt.inorder(bt.root)
    print("\nPostorder Binary Tree:", end=" ")
    bt.postorder(bt.root)
    print("\nPreorder Binary Tree:", end=" ")
    bt.preorder(bt.root)
