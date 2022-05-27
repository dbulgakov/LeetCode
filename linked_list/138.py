# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        connection_dict = {}
        head_start = head

        while head:
            connection_dict[head] = Node(head.val)
            head = head.next

        head = head_start

        while head:
            head_copy = connection_dict[head]
            head_copy.next = connection_dict[head.next] if head.next else None
            head_copy.random = connection_dict[head.random] if head.random else None

            head = head.next

        return connection_dict.get(head_start, None)
