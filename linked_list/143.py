from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return head

        slow = fast = head

        # find middle of a linked list:
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None

        # reverse the second part:
        while slow:
            tmp = slow
            slow = slow.next
            tmp.next = prev
            prev = tmp

        # merge results:
        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
