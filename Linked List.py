class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.start=None
        
    def InsertLast(self,value):
        NewNode=node(value)
        if self.start==None:
            
            self.start=NewNode
        else:
            temp=self.start
            
            while temp.next!=None:
                
                temp=temp.next
                
            temp.next=NewNode
    
    def DeleteFirst(self):
        
        if self.start==None:
            print("List is Empty")
            
        else:
            self.start=self.start.next
    def ViewList(self):
        
        if self.start==None:
            print("Linked List is Empty")
            
        else:
            temp=self.start
            
            while temp!=None:
                
                print(temp.data,end=" ")
                temp=temp.next
                
MyList=LinkedList()
size=int(input("enter the size of list"))
for _ in range(size):
    nums=int(input())
    MyList.InsertLast(nums)
MyList.ViewList()
print()
MyList.DeleteFirst()
MyList.ViewList()
