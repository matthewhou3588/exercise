### https://blog.csdn.net/qwas12345qwas/article/details/77727214


class Node:
    value = None
    left = None
    right = None

    def __init__(self, v):
        self.value = v



def construct(parent, index):
    print('index = {}'.format(index))
    if (index * 2 + 1) >= len(values):
        return

    if (index * 2 + 2) >= len(values):  # has left child
        left = Node(values[index * 2 + 1])
        parent.left = left
        return

    left = Node(values[index * 2 + 1])
    right = Node(values[index * 2 + 2])

    parent.left = left
    parent.right = right

    construct(left, index * 2 + 1)
    construct(right, index * 2 + 2)

    return parent

values = [6, 2, 3, 1, 4, 5, 7, 4, 10, 15]
root = Node(6)
construct(root, 0)

def tranverse(tree):
    if tree is not None:
        print(tree.value)
        tranverse(tree.left)
        tranverse(tree.right)

# tranverse(root)


DEPTH = 4
def Fun(tree, depth):
    if tree is None:
        return []
    if depth == DEPTH:
        return [tree.value]
    else:
        left = Fun(tree.left, depth+1)
        right = Fun(tree.right, depth+1)
        return left+right

result = Fun(root, 1)
print(result)
