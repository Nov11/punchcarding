# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        node = ListNode(0)
        ptr = node
        while l1 != None or l2 != None:
            if l1 == None:
                ptr.next = l2
                l2 = l2.next
            elif l2 == None:
                ptr.next = l1
                l1 = l1.next
            elif l1.val < l2.val:
                ptr.next = l1
                l1 = l1.next
            else:
                ptr.next = l2
                l2 = l2.next

            ptr = ptr.next
        return node.next