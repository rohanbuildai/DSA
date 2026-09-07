class Node :
    def __init__( self , data ) :
        self.data = data
        self.next = None
class LinkedList :
    def __init__( self ) :
        self.head = None

    def display(self):
    
        temp = self.head

        while temp:
            print(temp.data, end=" → ")
            temp = temp.next

        print("None")

    def add_one_to_a_number_represented_by_ll( self , head ) :

        temp = head
        prev = None

        while temp :
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front

        temp = prev
        carry = 1

        while temp :
            temp.data = temp.data + carry

            if temp.data < 10 :
                carry = 0
                break
            else :
                temp.data = 0
                carry = 1
            temp = temp.next

        temp = prev
        prev = None

        while temp:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front

        if carry == 1 :
            new_node = Node(1)
            new_node.next = prev
            return new_node

        return prev
        


ll = LinkedList()

ll.head = Node(9)
ll.head.next = Node(9)
ll.head.next.next = Node(9)
ll.head.next.next.next = Node(9)
ll.head.next.next.next.next = Node(9)

ll.head = ll.add_one_to_a_number_represented_by_ll(ll.head)

ll.display()