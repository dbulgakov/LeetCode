from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None

        res = ListNode(-1)
        res_start = res

        while head:
            if head.val != val:
                res.next = head
                res = res.next
            head = head.next

        res.next = None

        return res_start.next
