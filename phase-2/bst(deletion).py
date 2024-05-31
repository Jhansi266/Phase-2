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
def deletebst(root,val):
    if root==None:
        return None
    elif root.val>val:
        root.left=deletebst(root.left,val)
    elif root.val<val:
        root.right=deletebst(root.right,val)
    else:
        #no child
        if root.left==None and root.right==None:
            return None
        # 1 chlid
        if root.left==None:
            return root.right
        elif root.right==None:
            return root.left
        #2 child insus
        curr = root.right 
        while curr.left != None:
            curr = curr.left 
 
        
        root.val = curr.val 
        root.right = deletebst(root.right, curr.val)
    return root
 
        
#s=Node()
nums=[4,2,7,1,3,20]
root=None
for ele in nums:
    root=insertbst(root,ele)
printinorder(root)
print()
root = deletebst(root, 20)
printinorder(root)
print()
