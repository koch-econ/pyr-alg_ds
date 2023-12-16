# %%
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
root_node = TreeNode("A", node1, node2)

# упорядоченное дерево
#     B
#   A2   C2
# A1 A3 C1   C3
# %%


class Tree:
    "дерево"

    def __init__(self):
        self.root = None


def height(root):
    if root is None:
        return 0
    return max(height(root.left_child), height(root.right_child)) + 1


def getcol(h):
    if h == 1:
        return 1
    return getcol(h - 1) + getcol(h - 1) + 1


def printTree(M, root, col, row, height):
    if root is None:
        return
    M[row][col] = root.data
    printTree(M, root.left_child, col - pow(2, height - 2), row + 1, height - 1)
    printTree(M, root.right_child, col + pow(2, height - 2), row + 1, height - 1)


# %%


def TreePrinter():
    h = height(myTree.root)
    col = getcol(h)
    M = [[0 for _ in range(col)] for __ in range(h)]
    printTree(M, myTree.root, col // 2, 0, h)
    for i in M:
        for j in i:
            if j == 0:
                print(" ", end=" ")
            else:
                print(j, end=" ")
        print("")


# %%
myTree = Tree()
myTree.root = TreeNode(1)
myTree.root.left_child = TreeNode(2)
myTree.root.right_child = TreeNode(3)
myTree.root.left_child.left_child = TreeNode(4)
myTree.root.left_child.right_child = TreeNode(5)
myTree.root.right_child.left_child = TreeNode(6)
myTree.root.right_child.right_child = TreeNode(7)
TreePrinter()


# %%
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

    def pre_order(self, current_node):
        # Check if current_node exists
        if current_node:
            # Print the value of the current_node
            print(current_node.data)
            # Call pre_order recursively on the appropriate half of the tree
            self.pre_order(current_node.left_child)
            self.pre_order(current_node.right_child)


# %%
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
print(bst.search("b3"))

# %%[markdown]
# ### Обход деревьев
#
# https://ru.wikipedia.org/wiki/Обход_дерева


# %%
def in_order(current_node: TreeNode):
    # Если существует текущий узел
    if current_node:
        # обходим рекурсивно левое поддерево
        in_order(current_node.left_child)
        # печатаем узел
        print(current_node.data)
        # обходим рекурсивно правое поддерево
        in_order(current_node.right_child)


in_order(bst.root)


# %%
def pre_order(current_node):
    # Существует ли узел?
    if current_node:
        # печатаем значение верхнего узла
        print(current_node.data)
        # повторяем эту ф-ю на левом  и правом поддереве
        pre_order(current_node.left_child)
        pre_order(current_node.right_child)


op_tree = TreeNode("+", TreeNode(2), TreeNode("*", TreeNode(3), TreeNode(4)))

myTree = Tree()
myTree.root = op_tree
TreePrinter()
# %%
# Выдается префиксная запись выражения (Польская запись)
pre_order(op_tree)


# %%
def post_order(current_node):
    # Существует ли узел?
    if current_node:
        # повторяем эту ф-ю на левом  и правом поддереве
        pre_order(current_node.left_child)
        pre_order(current_node.right_child)
        # печатаем значение верхнего узла
        print(current_node.data)


post_order(op_tree)
# %%
# поуровневый обход (Breadth First Search, BFS)

# рекурсивная версия


# высота дерева
def height(root):
    if root is None:
        return 0
    return max(height(root.left_child), height(root.right_child)) + 1


def rec_breadth_first(root):
    for i in range(height(root)):
        print_level(root, i)


def print_level(root, level):
    if not root:
        return
    if level == 0:
        print(root.data)
    elif level > 0:
        print_level(root.left_child, level - 1)
        print_level(root.right_child, level - 1)


# %%
rec_breadth_first(bst.root)
# %%
import queue
from typing import Callable



def breadth_first(root_node: TreeNode, visit:Callable[[TreeNode],None]) -> None:
    q = queue.SimpleQueue()
    q.put(root_node)
    while not q.empty():
        node = q.get()
        visit(node)
        if node.left_child is not None:
            q.put(node.left_child)
        if node.right_child is not None:
            q.put(node.right_child)

#%%
breadth_first(bst.root, lambda node: print(node.data))
# %%
