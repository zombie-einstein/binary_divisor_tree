from asciitree import draw_tree

class node:
    "Divisor Tree Node"
    def __init__(self,n):
        self.n = n # Value of this node
        self.div = None # Child is divisor
        self.prm = None # Child is relative prime

    def addChild(self,m):
        "Add new node, or recursive call to next child node"
        if self.n == m : return
        if m % self.n == 0:
            if not self.div: self.div = node(m)
            else: self.div.addChild(m)
        else:
            if not self.prm: self.prm = node(m)
            else: self.prm.addChild(m)

def getNodeChildren(node):
    "Return iterable of a nodes children"
    ret = []
    if node.prm: ret.append(node.prm)
    if node.div: ret.append(node.div)
    return ret

def getNodeString(node):
    "Return nodes value as str"
    return str(node.n)

class divTree:
    "Divisor tree container"
    def __init__(self,i):
        self.root = node(i)
    
    def addNode(self,n):
        self.root.addChild(n)

    def printTree(self):
        print draw_tree(self.root,getNodeChildren,getNodeString)

A = divTree(2)
for i in range(3,8): A.addNode(i)

A.printTree()