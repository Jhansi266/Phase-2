class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def printlevelorder(root):
    if root==None:
        return
    q=[root]
    result=[]
    while len(q)>0:
        n=len(q)
        subres=[]
        for i in range(n):
            currnode=q.pop(0)#delete
            subres.append(currnode.data)#append
            if currnode.left!=None:#insert left
                q.append(currnode.left)
            if currnode.right!=None:#inser right
                q.append(currnode.right)
        result.append(subres)
    print(result)
def printLeftView(root):
        if root == None:
            return 
        Q = [root]
        result = []
        while len(Q) > 0:
           n = len(Q)
           for i in range(n):
            # step-1 (Deleting)
              currNode = Q.pop(0)
 
            # step-2 (Appending to result)
              if i == 0:
                  result.append(currNode.data)
 
            # step-3 (Enquing the left child)
              if currNode.left != None:
                  Q.append(currNode.left)
 
            # step-4 (Enquing the right child)
              if currNode.right != None:
                  Q.append(currNode.right)
 
        print("Left view is:", result)
def printRightView(root):
    if root == None:
        return 
    Q = [root]
    result = []
    while len(Q) > 0:
        n = len(Q)
        for i in range(n):
            # step-1 (Deleting)
            currNode = Q.pop(0)
 
            # step-2 (Appending to result)
            if i == n - 1:
                result.append(currNode.data)
 
            # step-3 (Enquing the left child)
            if currNode.left != None:
                Q.append(currNode.left)
 
            # step-4 (Enquing the right child)
            if currNode.right != None:
                Q.append(currNode.right)
 
    print("Right view is:", result)
obj1=Node(100)
obj2=Node(21)
obj3=Node(-151)
obj4=Node(87)
obj5=Node(12)
obj6=Node(52)
obj7=Node(8)
obj8=Node(27)
obj9=Node(28)
obj10=Node(7)


obj1.left=obj2
obj1.right=obj3
obj2.left=obj4
obj2.right=obj5
obj3.left=obj6
obj3.right=obj7
obj4.right=obj8
obj5.right=obj9
obj7.left=obj10
#printpreorder(obj1)
#printinorder(obj1)
#printpostorder(obj1)
printlevelorder(obj1)
printLeftView(obj1)
printRightView(obj1)


