class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root = None):
    if not root:
        return None
    else:
        return f'Node({root.val},{serialize(root.left)},{serialize(root.right)})'

def de_serialize(string):
    return eval(string)

h = Node(2)
l = Node(1)
r = Node(3)

h.left = l
h.left.left = r

print(serialize(h))
print(de_serialize(serialize(h)))
