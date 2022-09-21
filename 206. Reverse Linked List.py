# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution(ListNode):
    def reverseList(self, head: [ListNode]) -> [ListNode]:

        reverse = None
        while head:
            next = head.next
            head.next = reverse
            reverse = head
            head = next
        return reverse


head = [1,2,3,4,5]
a = Solution()
print(a.reverseList(head))
        
