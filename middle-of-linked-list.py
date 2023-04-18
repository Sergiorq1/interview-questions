# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.

# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        #makes a list based off the linked list.
        linked_into_list = []
        length_linked = 0
        #while head is true 
        #This loop loops through the entire linked list
        while head:
            #append current head
            linked_into_list.append(head)
            #add 1 to n
            length_linked += 1
            #traverse list
            head = head.next
        # divide n by 2 if n is even. Else, k equals ceiling of n/2
        k = length_linked // 2 if length_linked % 2 else (length_linked//2)+1
        #return the list with index being half length of list 
        return linked_into_list[k]
    
sol = Solution()
sol.middleNode([1,2,3,4,5])