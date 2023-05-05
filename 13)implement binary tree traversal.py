class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

def preorder_traversal(root):
    if root is None:
        return
    print(root.val, end=' ')
    preorder_traversal(root.left)
    preorder_traversal(root.right)

def inorder_traversal(root):
    if root is None:
        return
    inorder_traversal(root.left)
    print(root.val, end=' ')
    inorder_traversal(root.right)

def postorder_traversal(root):
    if root is None:
        return
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.val, end=' ')

def bfs_traversal(root):
    if root is None:
        return
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.val, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Example usage
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Preorder traversal:", end=' ')
preorder_traversal(root)
print()

print("Inorder traversal:", end=' ')
inorder_traversal(root)
print()

print("Postorder traversal:", end=' ')
postorder_traversal(root)
print()

print("BFS traversal:", end=' ')
bfs_traversal(root)
print()
