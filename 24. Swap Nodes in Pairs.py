# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def swapPairs1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        node = ListNode(0)
        node.next = head
        first = node.next

        while first != None and first.next != None:
            second = first.next
            second.val, first.val = first.val, second.val
            first = second.next
        return node.next

    def swapPairs(self, head):
        if head == None or head.next == None:
            return head
        node = ListNode(0)
        node.next = head

        first = node
        # first->first.next->first.next.next
        while first.next != None and first.next.next != None:
            last = first.next.next
            first.next.next = last.next
            last.next = first.next
            first.next = last
            first = last.next
        return node.next
