from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(-1)
        res_start = res

        to_next_node = 0

        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            el_sum = l1_val + l2_val + to_next_node

            if el_sum > 9:
                to_next_node = el_sum // 10
                el_sum = el_sum % 10
            else:
                to_next_node = 0

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            res.next = ListNode(el_sum)
            res = res.next

        if to_next_node:
            res.next = ListNode(to_next_node)

        return res_start.next
