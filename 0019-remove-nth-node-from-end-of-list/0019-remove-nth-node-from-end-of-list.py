# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        curr = head
        i = 1
        if (count - n) == 0:
            head = head.next
            return head
        while i < (count - n):
            curr = curr.next
            i = i + 1
        temp = curr.next
        curr.next = temp.next
        return head


