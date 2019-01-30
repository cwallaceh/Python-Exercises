# Flatten a binary tree into linked list
# Given a binary tree, flatten it into a linked list.
# After flattening, the left of each node should point to
# NULL and right should contain next node in level order.


class BinaryTree():
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

    def __repr__(self):
        return "BinaryNode(%s)" % str(self.data)


class Stack():
    def __init__(self):
        self.stack = []
        self.idx = 0

    def push(self, val):
        self.stack.append(val)
        self.idx += 1

    def pop(self):
        val = self.stack[self.idx - 1]
        del self.stack[self.idx - 1]
        self.idx -= 1
        return val

    def __repr__(self):
        return "Stack(%s)" % str(self.stack)


class Link:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return "%s→%s" % (self.value, self.next)


class LinkedList():
    def __init__(self, value):
        self.first = Link(value)
        self.current = self.first

    def __repr__(self):
        return 'LinkedList(%s)' % self.first

    def insert(self, value):
        self.current.next = Link(value)
        self.current = self.current.next


def flatten_tree_to_linked_list(root):
    """Traverse tree in depth frist fasion
    and add every node to the linked list"""
    stack = Stack()
    stack.push(root)
    while stack.stack:
        node = stack.pop()
        if 'linked' in locals():
            linked.insert(node.data)
        else:
            linked = LinkedList(node.data)
        if node.right:
            stack.push(node.right)

        if node.left:
            stack.push(node.left)

    return linked


root = BinaryTree()
root.data = 1
root.left = BinaryTree()
root.left.data = 2
root.right = BinaryTree()
root.right.data = 5
root.left.left = BinaryTree()
root.left.left.data = 3
root.left.right = BinaryTree()
root.left.right.data = 4
root.right.right = BinaryTree()
root.right.right.data = 6

ls = flatten_tree_to_linked_list(root)
print(ls)
# LinkedList(1→2→3→4→5→6→None)
