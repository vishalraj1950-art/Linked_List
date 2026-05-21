class Node():
    def __init__(self,data,next):
        self.data=data
        self.next=next


head = None

def create():
    global head
    def get()->int:
        x=int(input("enter data"))
        return x
    
    for i in range(5):
        if(head==None):
            head=Node(get(),None)
            itr=head
        else:
         node=Node(get(),None)
         itr.next=node
         itr=node
def travel():
    itr=head
    while itr:
        print(f"{itr.data}--->",end=
              "")
        itr=itr.next

create()
travel()
    
            
             
                 
                
            
        
    