class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # recursive solution:
        # base case:
        if not head or not head.next:
            return head
        # recursive call
        #new_head will eventually hold the head of the reversed list
        new_head = self.reverseList(head.next)
        # changes the next pointer of the node following the current head to point back to current head
        # this reverses the link direction for the current node
        head.next.next = head
        # disconnects the current node from the rest of the list, making sure it doesn't form a cycle
        head.next = None
        # after reversing the link for the current node, it returns "new head", the head of the newly created list
        return new_head