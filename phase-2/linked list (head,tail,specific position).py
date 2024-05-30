class node:
    def __init__(self,data):
        self.data=data
        self.next=None
def linkedlist(head):
    currentnode=head
    while currentnode!=None:
        print(currentnode.data,end="...>")
        currentnode=currentnode.next
    print()
def printtail(head,ele):
    temp=node(ele)
    if head==None:
        return temp
    tail=head
    while tail.next!=None:
        tail=tail.next
    tail.next=temp
    return head
def printhead(head,ele):
    temp=node(ele)
    temp.next=head
    return temp
def printposition(head,position,ele):
    if position==0:
        return printposition(head,ele)
    temp=node(ele)
    index=0
    currentnode=head
    while index!=position-1:
        currentnode=currentnode.next
        index+=1
    nextnode = currentnode.next 
    temp.next = nextnode 
    currentnode.next = temp 
    return head
nums=[10,20,30,40,50,60,70]
head=None
for ele in nums:
    head=printtail(head,ele)
    #linkedlist(head)
print("final list is:")
linkedlist(head)
head=printposition(head,3,19)
linkedlist(head)
