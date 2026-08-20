import math
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

    def remove_nt_node_from_the_back_of_linked_list(self , head , n) :

        # temp = head
        # count = 0

        # while temp :
        #     count += 1
        #     temp = temp.next

        # if n == count :
        #     return head.next

        # stopping_point = (count - n)

        # temp = head

        # while temp and stopping_point > 1 :
        #     temp = temp.next
        #     stopping_point -= 1

        # temp.next = temp.next.next

        # return head

        slow = head
        fast = head 

        for i in range (n) :
            fast = fast.next

        if fast is None :
            return head.next

        while fast and fast.next :
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next



ll = LinkedList()

ll.head = Node(1)
ll.head.next = Node(2)
ll.head.next.next = Node(3)
ll.head.next.next.next = Node(4)
ll.head.next.next.next.next = Node(5)

print(ll.remove_nt_node_from_the_back_of_linked_list(ll.head , 2))

ll.display()