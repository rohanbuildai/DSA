class Node :
    def __init__( self , data ) :
        self.data = data
        self.next = None
class LinkedList :
    def __init__( self ) :
        self.head = None
       
    def length_of_loop_in_linked_list( self , head ) :
        slow = head
        fast = head

        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast : 
                temp = slow
                count = 0

            
                while True :
                    count += 1
                    temp = temp.next

                    if temp == slow :
                        break
                    
                return count
        
        return 0

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
print(ll.length_of_loop_in_linked_list(ll.head))