class Node:
    def __init__(self,data,next):
        self.data=data
        self.next=next
    
class LinkedList:
    def __init__(self):
        self.head=None
        
    def insert_at_pos(self,pos:int,data):
        
        itr=self.head
        for i in range(1,pos-1):
            itr=itr.next
        node=Node(data,itr.next)
        itr.next=node
        
    def insert_at_begin(self,data):
        node=Node(data,None)
        node.data=data
        node.next=self.head
        self.head=node
    
    def insert_at_end(self,data):
        node=Node(data,None)
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=node
        
    def inset_Values(self,data_list:list):
        itr=self.head
        while itr.next:
            itr=itr.next
        for el in data_list:
            node=Node(el,None)
            itr.next=node
            itr=node
            
    def remove(self,pos):
        itr=self.head
        for i in range(1,pos-1):
            itr=itr.next
        itr.next=itr.next.next
            
        
        
        
    def travel(self):
        if(self.head==None):
            print("linked list is empty")
            return
        itr=self.head
        ll=""
        while itr:
            ll+=f"{itr.data}--->"
            itr=itr.next
        print(ll)
        return
            
ll1:LinkedList=LinkedList()
ll1.insert_at_begin(10)
ll1.insert_at_begin(20)
ll1.insert_at_begin(30)
ll1.travel()
ll1.insert_at_end(40)
ll1.insert_at_end(50)
ll1.insert_at_end(60)
ll1.travel()
ll1.insert_at_pos(3,45)
ll1.inset_Values(["banana","mango",5,"orange"])
ll1.travel()
ll1.remove(3)
ll1.travel()
ll1.remove(7)
ll1.travel()
        
            