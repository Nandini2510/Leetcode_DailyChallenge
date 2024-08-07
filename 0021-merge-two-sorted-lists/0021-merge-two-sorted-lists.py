# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 == None and l2 == None:
            return None
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        dummy = ListNode()
        curr = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        if l1 is None:
            curr.next = l2
        if l2 is None:
            curr.next = l1
        return dummy.next
        