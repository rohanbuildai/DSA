class Node :
    def __init__( self , data ) :
        self.data = data
        self.next = None
class LinkedList :
    def __init__( self ) :
        self.head = None

    def reverse_link_list(self , head) :
        # stack = []

        # temp = head

        # while temp :
        #     stack.append(temp.data)
        #     temp = temp.next

        # temp = head

        # while temp :
        #     temp.data = stack.pop()
        #     temp = temp.next

        # temp = head

        # return head.data

        temp = head
        prev = None

        while temp :
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev.data



ll = LinkedList()

ll.head = Node(3)
ll.head.next = Node(8)
ll.head.next.next = Node(7)
ll.head.next.next.next = Node(1)
ll.head.next.next.next.next = Node(3)
ll.head.next.next.next.next.next = Node(9)

print(ll.reverse_link_list(ll.head))