# Remove Node From End of Linked List
# Solved
# You are given the beginning of a linked list head, and an integer n.
#
# Remove the nth node from the end of the list and return the beginning of the list.
#
# Example 1:
#
# Input: head = [1,2,3,4], n = 2
#
# Output: [1,2,4]
# Example 2:
#
# Input: head = [5], n = 1
#
# Output: []
# Example 3:
#
# Input: head = [1,2], n = 2
#
# Output: [2]
# Constraints:
#
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
        def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
            dummy = ListNode(0, head)
            slow = fast = dummy

            for _ in range(n + 1):
                fast = fast.next

            while fast:
                fast = fast.next
                slow = slow.next

            slow.next = slow.next.next

            return dummy.next
