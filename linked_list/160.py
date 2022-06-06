from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def get_list_length(head: Optional[ListNode]):
            counter = 0

            while head:
                counter += 1
                head = head.next

            return counter

        len_a = get_list_length(headA)
        len_b = get_list_length(headB)
        diff = max(len_a, len_b) - min(len_a, len_b)

        longer = headA if len_a > len_b else headB
        shorter = headB if longer == headA else headA

        for i in range(diff):
            longer = longer.next

        while longer and shorter:
            if longer == shorter:
                return shorter
            shorter = shorter.next
            longer = longer.next

        return None
