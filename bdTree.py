class node:
    "Divisor Tree Node"
    def __init__(self,n):
        self.n = n # Value of this node
        self.div = None # Child is divisor
        self.prm = None # Child is relative prime

    def addChild(self,m):
        "Add new node, or recursive call to next child node"
        if self.n == m : return
        if self.m%n == 0:
            if not self.div: self.div = node(m)
            else: self.div.addChild(m)
        else:
            if not self.prm: self.prm = node(m)
            else: self.prm.addChild(m)

class divTree:
    "Divisor tree container"
    def __init__(self,i):
        self.root = node(i)
    
    def addNode(n):
        self.root.addChild(n)