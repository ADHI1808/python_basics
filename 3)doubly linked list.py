class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev= None

class Linked_list:
    def __init__(self):
        self.head = None

    def list(self,data):
        newnode = Node(data)
        newnode.next=None
        newnode.prev=None

        if self.head is None:
            self.head = newnode
            return
        temp = self.head
        while temp.next:
            temp=temp.next         
        temp.next = newnode
        

    def insert_first(self,data):
        newnode = Node(data)
        if self.head is None:
            self.head=newnode
            return
        else:
                   
            self.head.prev=newnode
            newnode.next=self.head
            self.head=newnode

    def insert_mid(self,data,pos):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            return
        else:
            temp=self.head
            i=1
            while(i<(pos-1)):
                temp=temp.next
                i=i+1
                
            newnode.next=temp.next
            temp.next=newnode
            temp.next.prev=newnode
            newnode.prev=temp


    def insert_last(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            return
        else:
            temp=self.head
            while temp.next:
                temp=temp.next         
        temp.next = newnode
        newnode.prev=temp

    def delete_first(self):
        if self.head is None:
            print("list is empty")
            
        else:
            self.head=self.head.next
            self.head.prev=None

    def delete_mid(self,pos):
        if self.head is None:
            print("list is empty")
        else:
            temp=self.head
            i=1
            while(i<(pos)):
                p=temp
                temp=temp.next
                i=i+1
            p.next=temp.next
            temp.next.prev=p
            
            


            
            
    def delete_last(self):
            if self.head is None:
                print("list is empty")
            else:
                temp=self.head
                while temp.next:
                    pre=temp
                    temp=temp.next
                pre.next=None
            

    def display(self):
        if self.head is None:
            return
        else:
            temp = self.head
            while temp is not None:
                d=hex(id(temp.next))
                print(temp.data,"<-->", end=' ')
                temp = temp.next

    
            
            
                
LL=Linked_list()
print("\n1.Create\n2.Insert_First\n3.Insert_Middle\n4.Insert_Last\n5.Delete_First\n6.Delete_Middle\n7.DeleteLast\n8.Exit")
while(True):             
    choice=int(input("\nenter the choice"))
    if choice==1:
        a=int(input("\nenter the node value"))
        LL.list(a)
        LL.display()
    elif choice==2:
        b=int(input("\nenter the node value insert at first"))
        LL.insert_first(b)
        LL.display()
    elif choice==3:
        pos=int(input("\nenter the position"))
        c=int(input("\nenter the node value insert at middle"))
        LL.insert_mid(c,pos)
        LL.display()
    elif choice==4:
        d=int(input("\nenter the node value insert at last"))
        LL.insert_last(d)
        LL.display()
    elif choice==5:
        LL.delete_first()
        LL.display()
    elif choice==6:
        pos=int(input("\nenter the position to delete"))
        LL.delete_mid(pos)
        LL.display()
    elif choice==7:
        LL.delete_last()
        LL.display()
    else:
        print("\nno choice")
        break
    
    
        
        
        
            
        

