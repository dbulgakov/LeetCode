# Definition for singly-linked list.
from typing import Optional
import math


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        counter = 0
        head_start = head

        while head is not None:
            counter += 1
            head = head.next

        center = counter // 2
        head = head_start
        counter = 0

        while head is not None:
            if counter == center:
                return head
            head = head.next
            counter += 1
