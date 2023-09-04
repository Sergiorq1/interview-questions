# Given two sorted linked lists, merge them so that the resulting linked list is also sorted.

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
      
class LinkedList:
    def __init__(self):
        self.head = None
    #adds element to the end of list
    #loops to the end of list to append there 
    def append(self, data):
        new_node = Node(data)
        #if linked-list is empty
        if self.head is None:
            self.head = new_node
            #end function
            return
        #if not empty
        #declare new variable
        current_node = self.head
        #while not at the end of list
        while current_node.next:
            current_node = current_node.next
            current_node.next = new_node
    #prints linked-list into list
    def print_list(self):
        new_list = []
        current_node = self.head
        while current_node:
            new_list.append(current_node.data)
            current_node = current_node.next
        print(new_list)

def merge_sorted_lists(list1, list2):
    # Create a new linked list, this will be printed later
    merged_list = LinkedList()
    # loop through both lists
    while list1 and list2:
        # compares both current nodes to see if list1's node is smaller
        if list1.data < list2.data:
            # append smaller node
            merged_list.append(list1.data)
            #go to next node for further comparison
            list1 = list1.next
        #if list2's current node is smaller 
        else:
            # append node
            merged_list.append(list2.data)
            # go to next node to continue loop
            list2 = list2.next
  ## These next lines of code fall outside of while loop
  # Append any remaining nodes from the first list
    while list1:
        merged_list.append(list1.data)
        list1 = list1.next

  # Append any remaining nodes from the second list
    while list2:
        merged_list.append(list2.data)
        list2 = list2.next
    return merged_list

list1 = LinkedList()
list1.append(1)
list1.append(2)
list1.append(4)
list1.append(5)
list1.append(23)
list1.append(123)
list1.append(258)
#[1,2,4,5,23,123,258]

list2 = LinkedList()
list2.append(1)
list2.append(3)
list2.append(4)
list2.append(12)
list2.append(234332)
#[1,3,4,12,234332]



merged_list = merge_sorted_lists(list1.head,list2.head)
merged_list.print_list()