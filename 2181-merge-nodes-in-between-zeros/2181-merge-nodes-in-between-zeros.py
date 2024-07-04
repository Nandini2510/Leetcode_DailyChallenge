# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        newHead = dummy
        sumVal = 0
        curr = head.next

        while curr:
            if curr.val == 0:
                newHead.next = ListNode(sumVal)
                newHead = newHead.next
                sumVal = 0
            else:
                sumVal += curr.val

            curr = curr.next
        return dummy.next

