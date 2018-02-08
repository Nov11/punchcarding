# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        node = ListNode(0)
        ptr = node
        # forward no
        # while len(lists) > 0:
        # to = 0
        # smallest = float('inf')
        # idx = -1
        # for i, v in enumerate(lists):
        #     if v != None:
        #         lists[i], lists[to] = lists[to], lists[i]
        #         if smallest > lists[to].val:
        #             smallest = lists[to].val
        #             idx = to
        #         to = to + 1
        # lists = lists[:to]
        # if idx != -1:
        #     ptr.next = ListNode(smallest)
        #     ptr = ptr.next
        #     lists[idx] = lists[idx].next

        # backward no
        #         last = len(lists) - 1
        #         while last >= 0:
        #             zero = last
        #             smallest = float('inf')
        #             idx = -1
        #             cur = 0
        #             while cur <= zero:
        #                 if lists[cur] == None:
        #                     lists[cur], lists[zero] = lists[zero], lists[cur]
        #                     zero = zero - 1
        #                 else:
        #                     if smallest > lists[cur].val:
        #                         smallest = lists[cur].val
        #                         idx = cur
        #                     cur = cur + 1

        #             if idx == -1:
        #                 break
        #             ptr.next = ListNode(smallest)
        #             ptr = ptr.next
        #             lists[idx] = lists[idx].next
        #             # lists = lists[:zero + 1]
        #             last = zero

        tmp = []
        for item in lists:
            while item:
                tmp.append(item.val)
                item = item.next
        tmp.sort()

        for item in tmp:
            ptr.next = ListNode(item)
            ptr = ptr.next

        return node.next


def toList(lst):
    node = ListNode(0)
    ptr = node
    for v in lst:
        ptr.next = ListNode(v)
        ptr = ptr.next
    return node.next


def gene(ll):
    result = []
    for v in ll:
        result.append(toList(v))
    return result


if __name__ == '__main__':
    s = Solution()
    p = gene(
        # [[]]
        [[1, 3, 4], [2, 6, 7]]
    )
    ret = s.mergeKLists(
        #
        p
    )
    while ret != None:
        print(ret.val)
        ret = ret.next

    tmp = [1, 2, 3, 4, 5, 6]
    k = tmp[:2] + tmp[3:]
    print(k)
