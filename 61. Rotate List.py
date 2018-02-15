# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        size = 0
        iter = head
        while iter != None:
            size = size + 1
            iter = iter.next
        if size < 2:
            return head
        k = k % size
        node = ListNode(0)
        node.next = head
        cur = node
        for i in range(k):
            cur = cur.next
        tail = node
        while cur.next != None:
            tail = tail.next
            cur = cur.next

        cur.next = node.next
        node.next = tail.next
        tail.next = None
        return node.next
