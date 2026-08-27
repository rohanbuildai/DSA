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

    def sort_linked_list_of_0s_1s_2s( self , head ) :

        # count0 = 0
        # count1 = 0
        # count2 = 0

        # temp = head

        # while temp :
        #     if temp.data == 0 :
        #         count0 += 1
        #     elif temp.data == 1 :
        #         count1 += 1
        #     elif temp.data == 2 :
        #         count2 += 1
        #     temp = temp.next

        # temp = head

        # while temp :

        #     if count0 :
        #         temp.data = 0
        #         count0 -= 1
        #     elif count1 :
        #         temp.data = 1
        #         count1 -= 1
        #     elif count2 :
        #         temp.data = 2
        #         count2 -= 1
        #     temp = temp.next

        # return head

        if head is None or head.next is None :
            return head

        zero_head = Node(-1)
        one_head = Node(-1)
        two_head = Node(-1)

        L0 = zero_head
        L1 = one_head
        L2 = two_head

        temp = head

        while temp :
            front = temp.next
            temp.next = None

            if temp.data == 0 :
                L0.next = temp
                L0 = temp
            elif temp.data == 1 :
                L1.next = temp
                L1 = temp
            elif temp.data == 2 :
                L2.next = temp
                L2 = temp
            temp = front

        L0.next = one_head.next if one_head.next else two_head.next
        L1.next = two_head.next
        L2.next = None

        new_head = zero_head.next
        return new_head



ll = LinkedList()

ll.head = Node(1)
ll.head.next = Node(0)
ll.head.next.next = Node(2)
ll.head.next.next.next = Node(0)
ll.head.next.next.next.next = Node(1)

ll.head = ll.sort_linked_list_of_0s_1s_2s(ll.head)

print(ll.head)


ll.display()
