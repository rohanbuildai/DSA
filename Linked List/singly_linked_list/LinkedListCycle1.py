class Node :
    def __init__( self , data ) :
        self.data = data
        self.next = None
class LinkedList :
    def __init__( self ) :
        self.head = None

    def detect_loop_in_a_linked_list (self , head) :

        # hash_map = {}

        # temp = head

        # while temp :

        #     if temp in hash_map :
        #         return True
            
        #     hash_map[temp] = 1

        #     temp = temp.next

        # return False


        # fast = head
        # slow = head

        # while fast and fast.next :

        #     slow = slow.next
        #     fast = fast.next.next

        #     if fast == slow :
        #         return True
        # return False


        fast = head
        slow = head

        while fast and fast.next :

            slow = slow.next
            fast = fast.next.next

            if fast == slow :
                return fast.data
        return False




# Create nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

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
print(ll.detect_loop_in_a_linked_list(ll.head))