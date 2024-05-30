class Node(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
#class Solution(object):
def maxLevelSum(root):
        if root==None:
            return
        q=[root]
        resultlevel=0
        resultsum=-100000000
        currlevel=1
        while len(q)>0:
           n=len(q)
           currsum=0
           for i in range(n):
                currNode=q.pop(0)#delete
                currsum+=currNode.val#append
                if currNode.left!=None:#insert left
                    q.append(currNode.left)
                if currNode.right!=None:#inser right
                    q.append(currNode.right)
           if currsum > resultsum:
                resultsum = currsum 
                resultlevel = currlevel 
           currlevel += 1


        print( resultlevel )   
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
#printlevelorder(obj1)
maxLevelSum(obj1)
