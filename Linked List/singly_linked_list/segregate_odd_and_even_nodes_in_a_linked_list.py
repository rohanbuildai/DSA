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

    def segregate_odd_and_even_nodes_in_a_linked_list( self , head ) :

        # values = []

        # temp = head
        # even = head.next
        # odd = head
        # i = 0

        # while odd and odd.next :
        #     values.append(odd.data)
        #     odd = odd.next.next
        # if odd : values.append(odd.data)

        # while even and even.next :
        #     values.append(even.data)
        #     even = even.next.next
        # if even : values.append(even.data)

        # while temp :
        #     temp.data = values[i]
        #     i+=1
        #     temp = temp.next

        # return head.data

        if head is None or head.next is None:
            return head

        even = head.next
        odd = head
        even_head = even

        while even and even.next :
            odd.next = odd.next.next
            odd = odd.next

            even.next = even.next.next
            even = even.next

        odd.next = even_head

        return head




ll = LinkedList()

ll.head = Node(1)
ll.head.next = Node(2)
ll.head.next.next = Node(3)
ll.head.next.next.next = Node(4)
ll.head.next.next.next.next = Node(5)

print(ll.segregate_odd_and_even_nodes_in_a_linked_list(ll.head))

ll.display()