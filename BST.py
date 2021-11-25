class bstNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = bstNode(data)
        else:
            cur = self.root
            while cur.left or cur.right:
                if data == cur.data:
                    return
                elif data < cur.data and cur.left:
                    cur = cur.left
                elif data < cur.data and not cur.left:
                    break
                elif data > cur.data and cur.right:
                    cur = cur.right
                elif data > cur.data and not cur.right:
                    break
            if data < cur.data:
                cur.left = bstNode(data)
            else:
                cur.right = bstNode(data)

    def print_helper(self, node):
        if not node:
            return
        self.print_helper(node.left)
        print(node.data)
        self.print_helper(node.right)

    def print_all(self):
        self.print_helper(self.root)

    def findTilt(self):
        val = [0]
        def dfsForTilt(node, val):
            if not node:
                return 0
            left = dfsForTilt(node.left, val)
            right = dfsForTilt(node.right, val)
            val[0] += abs(left-right)
            return node.data + left + right
        dfsForTilt(self.root, val)
        return val[0]

    def minDepth(self):
        def hlperMin(node):
            if not node:
                return 0
            return(1+max(hlperMin(node.left), hlperMin(node.right)))
        return hlperMin(self.root)

# tree = Bst()
#
# tree.insert(7)
# tree.insert(14)
# tree.insert(2)
# tree.insert(3)
#
# tree.insert(1)
# tree.insert(17)
# tree.insert(4)
# tree.insert(3)
# tree.insert(-1)
# tree.insert(5)
# tree.insert(9)
# tree.insert(13)
# tree.insert(2)
# tree.insert(0)
# tree.print_all()
# print(tree.minDepth())