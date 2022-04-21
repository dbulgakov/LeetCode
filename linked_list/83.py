from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        head_start = head
        prev = head

        while head:
            if head.val != prev.val:
                prev.next = head
                prev = head
            head = head.next

        prev.next = None

        return head_start
