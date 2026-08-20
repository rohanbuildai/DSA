class Node :
    def __init__( self , data ) :
        self.data = data
        self.next = None
class LinkedList :
    def __init__( self ) :
        self.head = None

    def linked_list_cycle_2(self , head) :

        fast = head
        slow = head

        while fast and fast.next :

            slow = slow.next
            fast = fast.next.next

            if slow == fast :

                slow = head

                while slow != fast :
                    slow = slow.next
                    fast = fast.next
                return slow.data

        return None


node1 = Node(3)
node2 = Node(2)
node3 = Node(0)
node4 = Node(-4)

# Connect nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

# Create LinkedList object
ll = LinkedList()

# Set head
ll.head = node1

# Call function
print(ll.linked_list_cycle_2(ll.head))