class Node :
    def __init__(self,data) :
        self.data = data
        self.next = None
class LinkedList :
    def __init__(self) :
        self.head = None

    def display(self) :
        temp = self.head

        while temp :
            print(temp.data,end="->")
            temp = temp.next
        print("None")

    def insertion_at_head(self,data) :
        new_node = Node(data)

        if self.head is None :
            self.head = new_node
            return 
        
        new_node.next = self.head
        self.head = new_node

    def deletion_at_head(self) :
        if self.head is None :
            print("Linked list is empty")
            return 

        self.head = self.head.next
    def deletion_at_tail(self):
        if self.head is None :
            return 
        if self.head.next is None :
            self.head = None
            return

        temp = self.head

        while temp.next.next :
            temp = temp.next
        temp.next = None

    def deletion_at_position(self,position) :
        prev = 0
        count = 0


        if self.head is None :
            return 
        if position == 1 :
            ll.deletion_at_head()
            return 
        temp = self.head

        while temp :
            count += 1

            if count == position :
                prev.next = prev.next.next
            prev = temp
            temp = temp.next

    def deletion_by_value(self,value) :
        prev = 0

        if self.head is None :
            return 
        
        if self.head.data == value :
            ll.deletion_at_head()
            return 

        temp = self.head

        while temp :
            if temp.data == value :
                prev.next = prev.next.next
            prev = temp
            temp = temp.next
        

ll = LinkedList()

ll.insertion_at_head(10)
ll.insertion_at_head(20)
ll.insertion_at_head(30)
# ll.deletion_at_head()
# ll.deletion_at_tail()
# ll.deletion_at_position(3)
ll.deletion_by_value(20)

ll.display()