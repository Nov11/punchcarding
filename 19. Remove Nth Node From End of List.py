# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        node = ListNode(0)
        node.next = head
        first = node
        last = node
        while n > 0:
            last = last.next
            n = n - 1

        while last.next != None:
            last = last.next
            first = first.next

        first.next = first.next.next

        return node.next