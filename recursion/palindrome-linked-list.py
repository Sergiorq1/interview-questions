# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ### recursion, if O(1) space required
        # Initialize a pointer to the head
        self.front_pointer = head

        # This function will use a pointer that starts at the head and advances with each recursive call.
        # It will compare the values of nodes from the front and back.
        def recursively_check(current_node: Optional[ListNode]) -> bool:
            #if not at the end of linked list
            if current_node is not None:
                # if the next node is empty 
                if not recursively_check(current_node.next):
                    return False
                # if the front_pointer value doesn't equal current_node value
                if self.front_pointer.val != current_node.val:
                    return False
                # go to next value
                self.front_pointer = self.front_pointer.next
            return True
        
        return recursively_check(head)

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(2)
node4 = ListNode(1)
node1.next = node2
node2.next = node3
node3.next = node4

solution = Solution()
print(solution.isPalindrome(node1))