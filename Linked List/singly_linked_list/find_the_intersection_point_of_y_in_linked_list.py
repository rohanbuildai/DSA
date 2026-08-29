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

    def find_the_intersection_point_of_y_in_linked_list( self , headA , headB ) :

        # hash_map = {}

        # temp = headA

        # while temp :
        #     hash_map[temp] = 1
        #     temp = temp.next

        # temp = headB

        # while temp :
        #     if temp in hash_map :
        #         return temp 
        #     temp = temp.next
        # return None

        t1 = headA
        count1 = 0

        while t1 :
            count1 += 1
            t1 = t1.next

        t2 = headB
        count2 = 0

        while t2 :
            count2 += 1
            t2 = t2.next

        difference = (count1-count2) if count1 > count2 else (count2-count1)

        temp1 = headA
        temp2 = headB

        if count1 > count2 :
            while difference > 0 :
                temp1 = temp1.next
                difference -= 1

        elif count2 > count1 :
            while difference > 0 :
                temp2 = temp2.next
                difference -= 1

        while temp2 and difference > 0 :
            temp2 = temp2.next
            difference -= 1

        while temp1 and temp2:

            if temp1 is temp2:
                return temp1

            temp1 = temp1.next
            temp2 = temp2.next

        return None


# Common nodes
node8 = Node(8)
node9 = Node(9)

node8.next = node9


# List A
node1 = Node(1)
node2 = Node(2)

node1.next = node2
node2.next = node8


# List B
node4 = Node(4)
node5 = Node(5)

node4.next = node5
node5.next = node8


ll = LinkedList()

intersection = ll.find_the_intersection_point_of_y_in_linked_list(
    node1,
    node4
)

print("\nList A:")
temp = node1

while temp:
    print(temp.data, end=" → ")
    temp = temp.next

print("None")


print("\nList B:")
temp = node4

while temp:
    print(temp.data, end=" → ")
    temp = temp.next

print("None")


print("\nIntersection check:")
if intersection:
    print("temp1:", intersection[0])
    print("temp2:", intersection[1])
else:
    print("No intersection")