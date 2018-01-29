# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k <= 1:
            return head

        node = ListNode(0)
        node.next = head

        ptr = node
        while ptr:
            tail = ptr
            for i in range(k):
                if tail == None:
                    break
                tail = tail.next
            if tail == None:
                break
            nextPtr = ptr.next
            ptr.next = tail.next
            iter = nextPtr
            end = tail.next
            while iter != end:
                tmp = iter.next
                iter.next = ptr.next
                ptr.next = iter
                iter = tmp
            ptr = nextPtr

        return node.next



