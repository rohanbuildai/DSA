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

    def delete_the_middle_node_in_linked_list(self , head) :

        # temp = head
        # count = 0

        # while temp :
        #     count += 1
        #     temp = temp.next

        # mid = math.floor(count / 2) + 1

        # temp = head
        # pointer = 1

        # while temp and pointer < mid-1 :
        #     pointer += 1
        #     temp = temp.next

        # temp.next = temp.next.next

        slow = head
        fast = head.next.next 

        while fast and fast.next :
            fast = fast.next.next
            slow = slow.next

        slow.next = slow.next.next



ll = LinkedList()

ll.head = Node(1)
ll.head.next = Node(2)
ll.head.next.next = Node(3)
ll.head.next.next.next = Node(4)
ll.head.next.next.next.next = Node(5)

print(ll.delete_the_middle_node_in_linked_list(ll.head))

ll.display()