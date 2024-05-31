class TreeNode:
     def __init__(self, val, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
#class Solution(object):
def printinorder(root):
    if root==None:
        return
    printinorder(root.left)
    print(root.val,end=',')
    printinorder(root.right)

def insertbst(root,val):
    if root==None:
        return TreeNode(val)
    elif root.val>val:
        root.left=insertbst(root.left,val)
    else:
        root.right=insertbst(root.right,val)
    return root
'''obj1=Node(100)
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
obj7.left=obj10'''
#s=Node()
nums=[4,2,7,1,3]
root=None
for ele in nums:
    root=insertbst(root,ele)
printinorder(root)



