import math
class Node :
    def __init__( self , val ) :
        self.val = val
        self.next = None
class LinkedList :
    def __init__( self ) :
        self.head = None

    def display(self):
    
        temp = self.head

        while temp:
            print(temp.val, end=" → ")
            temp = temp.next

        print("None")

    def sort_linked_list(self , head) :
        # temp = head
        # elements = []

        # while temp :
        #     elements.append(temp.val)
        #     temp = temp.next

        # elements.sort()

        # temp = head
        # i=0

        # while temp :
        #     temp.val = elements[i]
        #     temp = temp.next
        #     i+=1

        # return head.val

        def find_middle(head) :
            slow = head
            fast = head.next

            while fast and fast.next :
                slow = slow.next
                fast = fast.next.next

            return slow

        def merge_sort(head) :

            if head is None or head.next is None :
                return head

            mid = find_middle(head)

            left_head = head
            right_head = mid.next
            mid.next = None

            left_head = merge_sort(left_head)
            right_head = merge_sort(right_head)

            return merge(left_head , right_head)

        def merge(left_head , right_head) :
            dummy = Node(0)
            temp = dummy

            while left_head and right_head :

                if left_head.val <= right_head.val :
                    temp.next = left_head
                    left_head = left_head.next
                else:
                    temp.next = right_head
                    right_head = right_head.next

                temp = temp.next

            if left_head :
                temp.next = left_head

            if right_head :
                temp.next = right_head

            return dummy.next
        
        return merge_sort(head)



ll = LinkedList()

ll.head = Node(6)
ll.head.next = Node(5)
ll.head.next.next = Node(1)
ll.head.next.next.next = Node(2)
ll.head.next.next.next.next = Node(3)

ll.head = ll.sort_linked_list(ll.head)

ll.display()