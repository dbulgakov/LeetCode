# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]):
            res = ListNode(-1)
            res_start = res

            while list1 and list2:
                if list1.val > list2.val:
                    res.next = list2
                    list2 = list2.next
                else:
                    res.next = list1
                    list1 = list1.next

                res = res.next

            res.next = list1 if list1 else list2

            return res_start.next

        if not lists:
            return None

        result = lists[0]

        for i in range(1, len(lists)):
            result = merge_two_lists(result, lists[i])

        return result
