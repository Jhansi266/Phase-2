class node:
    def __init__(self,data):
        self.data=data
        self.next=None
def linkedlist(head):
    currentnode=head
    while currentnode!=None:
          print(currentnode.data,end="...> ")
          currentnode=currentnode.next
    print()
def listtail(head,ele):
        temp=node(ele)
        if head==None:
            return temp
        tail=head
        while  tail.next!=None:
            tail=tail.next
        tail.next=temp
        return head
def deletetail(head):
    if head==None or head.next==None:
        return None
    previous=None
    currentnode=head
    while currentnode.next!=None:
        previous=currentnode
        currentnode=currentnode.next
    previous.next=None
    return head
def deletehead(head):
    currentnode=head
    head.next=secondnode
    secondnode=currentnode
    
#nums=[71,72,73,74,75,76,77,78,79,80]
nums=[10,20,30,40,50,60]
head=None
for ele in nums:
    head=listtail(head,ele)
    linkedlist(head)
print("Final list is:")
linkedlist(head)

deletetail(head)
linkedlist(head)

'''linkedlist(head)
print("Final linked list is:")
linkedlist(head)'''
