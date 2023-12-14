#%%
# from https://www.geeksforgeeks.org/print-binary-tree-2-dimensions/

class TreeNode:
    """
    узел дерева 
    .data - полезная нагрузка 
    ссылка на корневой узел  правое поддерево
    """
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left_child = left
        self.right_child = right

node1 = TreeNode("B")
node2 = TreeNode("C")
root_node = TreeNode( "A",node1, node2)
#%%

class Tree:
    "дерево" 
    def __init__(self):
        self.root = None


def height(root):
    if root is None:
        return 0
    return max(height(root.left_child), height(root.right_child))+1


def getcol(h):
    if h == 1:
        return 1
    return getcol(h-1) + getcol(h-1) + 1


def printTree(M, root, col, row, height):
    if root is None:
        return
    M[row][col] = root.data
    printTree(M, root.left_child, col-pow(2, height-2), row+1, height-1)
    printTree(M, root.right_child, col+pow(2, height-2), row+1, height-1)

#%%

def TreePrinter():
    h = height(myTree.root)
    col = getcol(h)
    M = [[0 for _ in range(col)] for __ in range(h)]
    printTree(M, myTree.root, col//2, 0, h)
    for i in M:
        for j in i:
            if j == 0:
                print(" ", end=" ")
            else:
                print(j, end=" ")
        print("")

#%%
myTree=Tree()
myTree.root = TreeNode(1)
myTree.root.left_child = TreeNode(2)
myTree.root.right_child = TreeNode(3)
myTree.root.left_child.left_child = TreeNode(4)
myTree.root.left_child.right_child = TreeNode(5)
myTree.root.right_child.left_child = TreeNode(6)
myTree.root.right_child.right_child = TreeNode(7)
TreePrinter()
#%%
# %%
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def search(self, search_value):
        current_node = self.root
        while current_node:
            if search_value == current_node.data:
                return True
            if search_value < current_node.data:
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child
        return False
    def insert(self, data):
        new_node = TreeNode(data)
        # Check if the BST is empty
        if self.root is None:
            self.root = new_node
            return
        else:
            current_node = self.root
            while True:
                if current_node.data == data:
                    return 
                # Check if the data to insert is smaller than the current node's data
                if data < current_node.data:
                    if current_node.left_child is None:
                        current_node.left_child = new_node
                        return
                    else:
                        current_node = current_node.left_child
                # Check if the data to insert is greater than the current node's data
                elif data > current_node.data:
                    if current_node.right_child is None:
                        current_node.right_child = new_node
                        return
                    else:
                        current_node = current_node.right_child
#%%
bst = BinarySearchTree()

bst.insert("c1")
bst.insert("b2")
bst.insert("b1")
bst.insert("b3")
bst.insert("d2")
bst.insert("d1")
bst.insert("d3")
myTree = bst
TreePrinter()
# %%
print(bst.search( "b3"))

# %%
