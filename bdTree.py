from binarytree import Node, pprint, inspect
from fractions import gcd

class nData:
    "Store values for each node"
    def __init__(self,n,l,r,h):
        self.val = n
        self.lft = l
        self.rgt = r
        self.hgt = h
    
    def __str__(self):
        return str(self.val)+":"+str(self.hgt)+"["+str(self.lft)+","+str(self.rgt)+"]" 

class divNode(Node):
    "Divisor Tree Node"
    def __init__(self,n,l,r,h):
        Node.__init__(self,nData(n,l,r,h)) 
    
    def __str__(self):
        return self.value.str()

    def addChild(self,m):
        "Add new node, or recursive call to next child node"
        if self.value.val == m : return
        #if gcd(m,self.value.val) > 1:
        if m % self.value.val == 0:
            if not self.left: self.left = divNode(m,self.value.lft+1,self.value.rgt,self.value.hgt+1)
            else: self.left.addChild(m)
        else:
            if not self.right: self.right = divNode(m,self.value.lft,self.value.rgt+1,self.value.hgt+1)
            else: self.right.addChild(m)

class divTree:
    "Divisor tree container, initialize as single node or from list of values"
    def __init__(self,i):
        if isinstance(i,(int,long)):
            self.root = divNode(i,0,0,0)
        elif isinstance(i,list):
            self.root = divNode(i[0],0,0,0)
            for j in i[1:]: self.addNode(j)
    
    def addNode(self,n):
        "Add and propogate new node to tree"
        self.root.addChild(n)

    def printTree(self):
        "Use binarytree to print tree"
        pprint(self.root)

    def getProperties(self):
        "Inspect divTree's properties"
        return inspect(self.root)