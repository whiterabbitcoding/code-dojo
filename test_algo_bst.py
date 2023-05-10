import collections

Node = collections.namedtuple("Node", ["left", "right", "value"])


n1 = Node(value=1, left=None, right=None)
n3 = Node(value=3, left=None, right=None)
n2 = Node(value=2, left=n1, right=n3)

print(n2.left)
print(n2.right)
print(n2.value)


class BinaryTree:
    def __init__(self, root_node: Node):
        self.root_node = root_node

    def lookup(self, lookup_value: int):
        node = self.root_node
        if node.left.value < lookup_value:
            if node.right.value > lookup_value:
                BinaryTree(node.right).lookup(lookup_value)
            elif node.right.value == lookup_value:
                return True
            elif node.right.value < lookup_value:
                return False
        elif node.left.value > lookup_value:
            BinaryTree(node.right).lookup(lookup_value)
        elif node.left.value == lookup_value:
            return True


def contains(root, value):
    return BinaryTree(root).lookup(value)


print(contains(n2, 1))


# class BinaryTree:
#     def __init__(self, rootdata):
#         print(rootdata)
#         self.root = collections.namedtuple(
#             "Node", [rootdata.get("left"), rootdata.get("right"), rootdata.get("value")]
#         )

#     def LOOKUP(self, lookupval):

#         if lookupval < self.root.get("value"):
#             if self.root.left:
#                 return BinaryTree(self.root.left).LOOKUP(
#                     lookupval
#                 )  # recursively check the left tree
#             else:
#                 return False  # can't go any further- so return false
#         elif lookupval > self.root.get("value"):
#             if self.root.right:
#                 return BinaryTree(self.root.right).LOOKUP(lookupval)
#             else:
#                 return False
#         else:
#             return True
