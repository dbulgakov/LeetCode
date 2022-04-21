from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f'val={self.val} | next={self.next}'


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        res = ListNode(-1, head)
        pred = res

        while head and head.next:
            if head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                pred.next = head.next
            else:
                pred = pred.next
            head = head.next
        return res.next
