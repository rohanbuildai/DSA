import math
class Node :
    def __init__( self , data ) :
        self.data = data
        self.next = None
class LinkedList :
    def __init__( self ) :
        self.head = None

    def middle_of_linkedlist( self , head ) :

        # count=0
        # temp = head

        # while temp :
        #     count += 1
        #     temp = temp.next

        # if ( count%2 != 0) :
        #     temp = head
        #     middle = math.ceil(count/2)

        #     for i in range (1,middle) :
        #         temp = temp.next

        #     return temp.data

        # if ( count%2 == 0) :
        #     temp = head
        #     middle = count // 2 + 1

        #     for i in range (1,middle) :
        #         temp = temp.next

        #     return temp.data


        slow = head
        fast=head

        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next

        return slow.data


ll = LinkedList()

ll.head = Node(3)
ll.head.next = Node(8)
ll.head.next.next = Node(7)
ll.head.next.next.next = Node(1)
ll.head.next.next.next.next = Node(3)
ll.head.next.next.next.next.next = Node(9)

print(ll.middle_of_linkedlist(ll.head))