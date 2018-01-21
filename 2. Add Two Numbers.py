# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        carry = 0
        node = ListNode(0)
        cur = node
        while l1 != None or l2 != None or carry != 0:
            v = carry
            if l1 != None:
                v = v + l1.val
                l1 = l1.next
            if l2 != None:
                v = v + l2.val
                l2 = l2.next

            cur.next = ListNode(v % 10)
            cur = cur.next
            carry = v // 10

        return node.next
