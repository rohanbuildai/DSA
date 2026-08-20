class Node :
    def __init__( self , val ) :
        self.val = val
        self.next = None
class LinkedList :
    def __init__( self ) :
        self.head = None

    def check_if_a_linked_list_is_palinfrome_or_not (self , head) :

        slow = head
        fast = head

        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next


        mid = slow
        prev = None

        while mid :
            front = mid.next
            mid.next = prev
            prev = mid
            mid = front

        first = head
        second = prev

        while second :
            if first.val != second.val :
                return False

            second = second.next
            first = first.next

        return True

        


node1 = Node(1)
node2 = Node(2)
node3 = Node(2)
node4 = Node(1)

# Connect nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = None

# Create LinkedList object
ll = LinkedList()

# Set head
ll.head = node1

# Call function
print(ll.check_if_a_linked_list_is_palinfrome_or_not(ll.head))