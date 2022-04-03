class Node:  # This is a struct node
    def __init__(self,val):
        self.val=val
        self.next=None

class List:
    def __init__(self):
        self.head=None
    
    def push_back(self, integer_val):
        new_Node = Node(integer_val)
        if self.head == None:
            self.head = new_Node
        elif self.head != None:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = new_Node    
    
    def print(self):
        if self.head == None:
            return None
        elif self.head != None:
            temp = self.head 
            numbers = []
            while temp != None:
                numbers.append(temp.val)
                temp = temp.next 
            print(numbers)

new_List = List()
new_List.push_back(3)
new_List.push_back(5)
new_List.push_back(10)
new_List.push_back(11)
new_List.print()   