from binarytree import Node, pprint

class divNode(Node):
    "Divisor Tree Node"
    def __init__(self,n):
        Node.__init__(self,n) 
        
    def addChild(self,m):
        "Add new node, or recursive call to next child node"
        if self.value == m : return
        if m % self.value == 0:
            if not self.left: self.left = divNode(m)
            else: self.left.addChild(m)
        else:
            if not self.right: self.right = divNode(m)
            else: self.right.addChild(m)

class divTree:
    "Divisor tree container, initialize as single node or from list of values"
    def __init__(self,i):
        if isinstance(i,(int,long)):
            self.root = divNode(i)
        elif isinstance(i,list):
            self.root = divNode(i[0])
            for j in i[1:]: self.addNode(j)
    
    def addNode(self,n):
        "Add and propogate new node to tree"
        self.root.addChild(n)

    def printTree(self):
        "Use binarytree to print tree"
        pprint(self.root)